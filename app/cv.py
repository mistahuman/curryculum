import subprocess, os
from jinja2 import Environment, FileSystemLoader, select_autoescape
import argparse
from app.exceptions import InvalidInput, ErrorTemplate, GenerationError
from app.utils import import_cvdata

DEFAULT_IMG = 'mycv/user.jpg'


class CVMaker:

    def __init__(self, path_output: str) -> None:

        if not os.path.isdir(path_output):
            os.mkdir(path_output)

        self.path_output = path_output

    @staticmethod
    def escape_latex(text):
        """
        The special characters are:
            \ = command character
            { = open group
            } = end group
            & = table column separator
            # = parameter specifier
            % = comment character
            _ = subscript
            ^ = superscript
            ~ = non-breakable space
            $ = mathematics mode
        """
        latex_special_chars = ["#", "$", "%", "&", "_", "{", "}", "~", "^"]

        for char in latex_special_chars:
            text = text.replace(char, "\\" + char)

        return text

    def set_data(self, data: object) -> None:
        # check data.. TODO validation
        if not data:
            raise InvalidInput("Invalid data.")

        self.__configure_data(data)

    def set_template(self, template_path: str) -> None:
        # check data.. TODO validation
        if not os.path.isfile(template_path):
            raise InvalidInput("Invalid template data.")
        self.__render_template(template_path)
        

    def compiler_cv(self, template_name: str):
        self.set_template(template_name)
        self.__compiler_tex()
        self.__load_pdf()

    def __configure_data(self, data: object) -> None:
        self.cv_content = None
        self.blob_pdf = None

        self.output_name = os.path.join(
            self.path_output, "-".join(["cv", str(data.get("code"))])
        )
        self.worker_data = data
        if not self.worker_data.get("url_pic") or not os.path.isfile(self.worker_data.get("url_pic")):
            self.worker_data["url_pic"] = os.path.join(DEFAULT_IMG) 

    def __render_template(self, template_path):
        try:
            jinjaenv = Environment(
                autoescape=False,
                block_start_string=r"\BLOCK{",
                block_end_string=r"}",
                variable_start_string=r"\VAR{",
                variable_end_string=r"}",
                comment_start_string=r"\#{",
                comment_end_string=r"}",
                line_statement_prefix=r"%%",
                line_comment_prefix=r"%#",
                trim_blocks=True,
                extensions=["jinja2.ext.i18n"],
                loader=FileSystemLoader("."),
            )
            jinjaenv.comment_start_string = "//"
            jinjaenv.filters["escape_latex"] = self.escape_latex

            template = jinjaenv.get_template(template_path)
            # render template
            self.cv_content = template.render(self.worker_data)

        except Exception as exp:
            raise ErrorTemplate(f"Error rendering data over template. {exp}")

    def __compiler_tex(self):
        if not self.cv_content:
            raise GenerationError("Compiling error, content not found.")
        try:
            path_tex = self.output_name + ".tex"
            # write new tex
            with open(path_tex, "w") as f:
                f.write(self.cv_content)
            # compile with pdflatex
            subprocess.run(
                [
                    "pdflatex",
                    "-interaction",
                    "nonstopmode",
                    "-output-directory",
                    os.path.dirname(path_tex),
                    path_tex,
                ]
            )
        except Exception as exp:
            raise GenerationError(f"Latex error. {exp}")

    def __load_pdf(self):
        filename = self.output_name + ".pdf"
        if not os.path.isfile(filename):
            raise GenerationError(f"Pdf {filename} not found.")
        
        with open(filename, "rb") as file:
            self.blob_pdf = file.read()




### TEST MAIN

if __name__ == "__main__":
    TEMPLATE_DEFAULT2 = "templates/europecv_template.tex"
    TEMPLATE_DEFAULT3 = "templates/moderncv_template.tex"
    TEMPLATE_CVDATA = "mycv/mycv-demo.json"
    OUTPUT_DEFAULT = 'output/'
    
    try:
        parser = argparse.ArgumentParser(prog='Curryculum',description='Make your boring cv smartly')
        parser.add_argument('-m', metavar="mode", dest="mode", required=False, default="console-app", help="Console or Web")
        parser.add_argument('-t', metavar="template_file", dest="template", required=False, default=TEMPLATE_DEFAULT3, help="Input template file")
        parser.add_argument('-o', metavar="output_dir", dest="output", required=False, default=OUTPUT_DEFAULT, help="Output dir")
        parser.add_argument('-i', metavar="input_data", dest="input_data", required=False, default=TEMPLATE_CVDATA, help="Input CV data")
        args = parser.parse_args()

        my_cvdata = import_cvdata(args.input_data)

        ## cv maker 
        obj = CVMaker(args.output)
        obj.set_data(my_cvdata)
        obj.compiler_cv(args.template)
        print(f"CV generated {obj.output_name} with template {args.template}.")


    except InvalidInput as err:
        print(f"Not valid data. {err}")
    except ErrorTemplate as err:
        print(f"Template error. {err}")
    except GenerationError as err:
        print(f"Generation error. {err}")
    except Exception as err:
        print(f"Generic exception. {err}")