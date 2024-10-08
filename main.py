from app.cv import CVMaker, InvalidInput, ErrorTemplate, GenerationError, import_cvdata
import argparse
from fastapi import FastAPI, WebSocket
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import uvicorn


MENU = [
    {
        "label": "Europass",
        "tag": "europass",
        "template_path": "templates/europass_template.tex"
    },
    {
        "label": "AltaCV",
        "tag": "altacv",
        "template_path": "templates/altacv_template.tex"
    }
]

TEMPLATE_DEFAULT1 = "templates/europass_template.tex"
TEMPLATE_CVDATA = "mycv/mycv.json"
OUTPUT_DEFAULT = 'output/'

try:
    parser = argparse.ArgumentParser(prog='Curryculum',description='Make your boring cv smartly')
    parser.add_argument('-m', metavar="mode", dest="mode", required=False, default="console-app", help="Console or Web")
    parser.add_argument('-t', metavar="template_file", dest="template", required=False, default=TEMPLATE_DEFAULT1, help="Input template file")
    parser.add_argument('-o', metavar="output_dir", dest="output", required=False, default=OUTPUT_DEFAULT, help="Output dir")
    parser.add_argument('-i', metavar="input_data", dest="input_data", required=False, default=TEMPLATE_CVDATA, help="Input CV data")
    args = parser.parse_args()

    my_cvdata = import_cvdata(args.input_data)
    
    ## cv maker 
    cv_maker = CVMaker(args.output)
    cv_maker.set_data(my_cvdata)

    # set fastapi 
    app = FastAPI()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.get("/api/menu")
    async def get_data():
        return MENU

    @app.get("/api/prevdata")
    async def get_data():
        return cv_maker.worker_data

    @app.post("/api/compile-cv")
    async def compiler_cv():
        cv_maker.compiler_cv(args.template)
        print(f"CV generated {cv_maker.output_name} with template {args.template}.")



    app.mount("/", StaticFiles(directory="ui/build", html=True), name="static")

    if __name__ == "__main__":
        uvicorn.run(app, host="127.0.0.1", port=8000)


except InvalidInput as err:
    print(f"Not valid data. {err}")
except ErrorTemplate as err:
    print(f"Template error. {err}")
except GenerationError as err:
    print(f"Generation error. {err}")
except Exception as err:
    print(f"Generic exception. {err}")
