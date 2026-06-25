from flask import Flask, render_template, request, jsonify, send_file
from detector import check_url
from reportlab.pdfgen import canvas
from datetime import datetime

app = Flask(__name__)

history = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/check", methods=["POST"])
def check():

    data = request.get_json()
    url = data.get("url")

    result = check_url(url)

    history.append({
        "url": url,
        "status": result["status"],
        "score": result["score"],
        "reasons": result["reasons"]
    })

    return jsonify(result)

@app.route("/history")
def get_history():
    return jsonify(history)

@app.route("/download")
def download():

    pdf = canvas.Canvas("report.pdf")

    pdf.setTitle("Phishing URL Detection Report")

    pdf.setFont("Helvetica-Bold", 18)
    pdf.drawString(150, 800, "Phishing URL Detection Report")

    pdf.setFont("Helvetica", 12)

    current_time = datetime.now().strftime(
        "%d-%m-%Y %I:%M %p"
    )

    pdf.drawString(
        50,
        770,
        f"Generated On: {current_time}"
    )

    y = 730

    for index, item in enumerate(history, start=1):

        pdf.setFont("Helvetica-Bold", 12)

        pdf.drawString(
            50,
            y,
            f"Scan #{index}"
        )

        y -= 25

        pdf.setFont("Helvetica", 11)

        pdf.drawString(
            70,
            y,
            f"URL: {item['url']}"
        )

        y -= 20

        pdf.drawString(
            70,
            y,
            f"Status: {item['status']}"
        )

        y -= 20

        pdf.drawString(
            70,
            y,
            f"Risk Score: {item['score']}%"
        )
        
        pdf.drawString(
            70,
            y,
            "Reasons:"
        )

        y -= 20

        for reason in item["reasons"]:

            pdf.drawString(
                90,
                y,
                f"- {reason}"
            )

            y -= 20

        y -= 35

        if y < 100:
            pdf.showPage()
            y = 800

    pdf.save()

    return send_file(
        "report.pdf",
        as_attachment=True
    )
    

if __name__ == "__main__":
    app.run(debug=True)