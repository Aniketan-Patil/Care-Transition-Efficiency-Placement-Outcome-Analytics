import plotly.graph_objects as go


def create_pipeline_sankey(df):

    apprehended = df["CBP_Apprehended"].sum()

    custody = df["CBP_Custody"].sum()

    transferred = df["CBP_Transferred"].sum()

    hhs = df["HHS_Care"].mean()

    discharged = df["HHS_Discharged"].sum()

    fig = go.Figure(
        data=[
            go.Sankey(
                node=dict(
                    label=[
                        "Apprehended",
                        "CBP Custody",
                        "Transferred",
                        "HHS Care",
                        "Discharged"
                    ]
                ),

                link=dict(
                    source=[0, 1, 2, 3],

                    target=[1, 2, 3, 4],

                    value=[
                        apprehended,
                        transferred,
                        transferred,
                        discharged
                    ]
                )
            )
        ]
    )

    fig.update_layout(
        title="Care Pipeline Flow"
    )

    return fig