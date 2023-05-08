from flask import Flask, render_template, request, make_response
import pickle
# from weasyprint import HTML
# from  wkhtmltopdf import wkhtmltopdf
# import imp

# module_path = 'c:\\users\\lenovo\\desktop\\medify_diseaseprediction\\venv\\lib\\site-packages\\wkhtmltopdf\\__init__.py'

# wkhtmltopdf = imp.load_source('my_module', module_path)

# from wkhtmltopdf.main import WKhtmlToPdf

# import pdfkit
# import venv 
# config = pdfkit.configuration(wkhtmltopdf='venv\sS  ')

from predict_disease import predict_disease
# from waitress import serve

app = Flask(__name__)

with open('models/symptoms.plk', 'rb') as f:
    symptoms = pickle.load(f)

with open('models/RandomForestClassifier.plk', 'rb') as f:
    rfc = pickle.load(f)

with open('./models/precaution_dict.plk', 'rb') as f:
    precaution_dict = pickle.load(f)


@app.route('/')
def index():
    return render_template('index.html', symptoms=symptoms)


# @app.route('/predict', methods=['POST'])
# def predict():
#     user_input = list(request.form.values())

#     # Remove empty strings if any
#     while '' in user_input:
#         user_input.remove('')
    
#     out = render_template('predict.html',  prediction=predict_disease(user_input, rfc), precaution=precaution_dict)
#     return out


@app.route('/predict', methods=['POST'])
def predict():
    user_input = list(request.form.values())

    # Remove empty strings if any
    while '' in user_input:
        user_input.remove('')
    
    out = render_template('predict.html',  prediction=predict_disease(user_input, rfc), precaution=precaution_dict)
    return out

    # pdf = pdfkit.from_string(out, options=options)
    # pdf = pdfkit.from_string(out)
    # return Response(pdf, mimetype="application/pdf")



# @app.route("/generateReport")
# def report():
    # html = render_template("predict.html")
    # pdf = pdfkit.from_string(html, False)
    # response = make_response(pdf)
    # response.headers["Content-Type"] = "application/pdf"
    # response.headers["Content-Disposition"] = "inline; filename=output.pdf"
    # return response



# @app.route("/download")
# def route_download():
    
#     # Get the HTML output
#     out = render_template("predict.html")
    
#     # PDF options
#     options = {
#         "orientation": "landscape",
#         "page-size": "A4",
#         "margin-top": "1.0cm",
#         "margin-right": "1.0cm",
#         "margin-bottom": "1.0cm",
#         "margin-left": "1.0cm",
#         "encoding": "UTF-8",
#     }
    
#     # Build PDF from HTML 
#     pdf = pdfkit.from_string(out, options=options)
    
#     # Download the PDF
#     return Response(pdf, mimetype="application/pdf")
    


if __name__ == "__main__":
    app.run(debug=True)

# if __name__ == '__main__':

#     serve(app, host="0.0.0.0", port=8080)
