from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak
)

from reportlab.lib.styles import getSampleStyleSheet

from datetime import datetime


def generate_pdf_report(
    metrics,
    mae,
    rmse,
    r2,
    df
):

    filename = "reports/Care_Transition_Report.pdf"

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    elements = []

    elements.append(
        Paragraph(
            "Care Transition Efficiency & Placement Outcome Analytics",
            styles["Title"]
        )
    )

    elements.append(
        Paragraph(
            "Executive Summary Report",
            styles["Heading2"]
        )
    )

    elements.append(Spacer(1, 20))

    elements.append(
        Paragraph(
            f"Generated On: {datetime.now().strftime('%d-%m-%Y')}",
            styles["BodyText"]
        )
    )

    elements.append(Spacer(1, 20))

    elements.append(
        Paragraph(
            "Project Overview",
            styles["Heading2"]
        )
    )

    elements.append(
        Paragraph(
            """
            This report evaluates operational efficiency
            within the care transition pipeline by analyzing
            transfer performance, placement outcomes,
            backlog accumulation, and forecasting trends.
            """,
            styles["BodyText"]
        )
    )

    elements.append(Spacer(1, 20))

    elements.append(
        Paragraph(
            "Key Performance Indicators",
            styles["Heading2"]
        )
    )

    elements.append(
        Paragraph(
            f"Total Apprehended: {metrics['Total Apprehended']:,}",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"Total Transfers: {metrics['Total Transfers']:,}",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"Total Discharged: {metrics['Total Discharged']:,}",
            styles["BodyText"]
        )
    )

    avg_transfer = df["Transfer_Efficiency"].mean()
    avg_discharge = df["Discharge_Effectiveness"].mean()

    elements.append(Spacer(1, 20))

    elements.append(
        Paragraph(
            "Operational Assessment",
            styles["Heading2"]
        )
    )

    elements.append(
        Paragraph(
            f"Average Transfer Efficiency: {avg_transfer:.2f}%",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"Average Discharge Effectiveness: {avg_discharge:.2f}%",
            styles["BodyText"]
        )
    )

    elements.append(Spacer(1, 20))

    elements.append(
        Paragraph(
            "Forecasting Performance",
            styles["Heading2"]
        )
    )

    elements.append(
        Paragraph(
            f"MAE: {mae:.2f}",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"RMSE: {rmse:.2f}",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"R² Score: {r2:.3f}",
            styles["BodyText"]
        )
    )

    elements.append(Spacer(1, 20))

    elements.append(
        Paragraph(
            "Executive Recommendations",
            styles["Heading2"]
        )
    )

    elements.append(
        Paragraph(
            """
            • Improve transfer efficiency between care stages.<br/>
            • Reduce backlog accumulation through proactive monitoring.<br/>
            • Strengthen placement outcome tracking.<br/>
            • Continue forecasting to anticipate future workload trends.
            """,
            styles["BodyText"]
        )
    )

    elements.append(Spacer(1, 20))

    elements.append(
        Paragraph(
            "Prepared using Care Transition Efficiency & Placement Outcome Analytics",
            styles["Italic"]
        )
    )

    doc.build(elements)

    return filename