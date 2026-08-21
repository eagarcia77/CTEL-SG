from pathlib import Path
from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.staticfiles import StaticFiles
from formatter import format_uploaded_module

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / 'outputs'
OUTPUT_DIR.mkdir(exist_ok=True)

app = FastAPI(title='APA 7 Module Formatter', version='1.0.0')
app.mount('/static', StaticFiles(directory=BASE_DIR / 'static'), name='static')
templates = Jinja2Templates(directory=BASE_DIR / 'templates')

@app.get('/', response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse('index.html', {'request': request, 'result': None})

@app.post('/format', response_class=HTMLResponse)
async def format_module(
    request: Request,
    file: UploadFile = File(...),
    profile: str = Form('blackboard'),
    font: str = Form('Arial'),
    font_size: float = Form(11),
):
    suffix = Path(file.filename or '').suffix.lower()
    if suffix not in {'.docx', '.pdf', '.html', '.htm', '.txt'}:
        raise HTTPException(400, 'Formato no compatible. Use DOCX, PDF, HTML, HTM o TXT.')

    data = await file.read()
    if len(data) > 30 * 1024 * 1024:
        raise HTTPException(413, 'El archivo excede 30 MB.')

    try:
        result = format_uploaded_module(
            filename=file.filename or f'modulo{suffix}',
            data=data,
            output_dir=OUTPUT_DIR,
            profile=profile,
            font=font,
            font_size=font_size,
        )
    except Exception as exc:
        raise HTTPException(500, f'No se pudo procesar el archivo: {exc}') from exc

    return templates.TemplateResponse('index.html', {'request': request, 'result': result})

@app.get('/download/{filename}')
async def download(filename: str):
    safe = Path(filename).name
    path = OUTPUT_DIR / safe
    if not path.exists():
        raise HTTPException(404, 'Archivo no encontrado.')
    return FileResponse(path, filename=safe)
