tab1, tab2, tab3, tab4, tab5 = st.tabs(
    ["📊 KPIs", "📄 Tabla", "📊 Barras", "📈 Scatter", "🔵 Bubble Chart"]
)


with tab5:
    st.subheader("🔵 Relación Deserción vs Empleabilidad vs Capital Recuperable")
    fig_bubble = px.scatter(
        df,
        x="Desercion_SIES_pct",
        y="Empleabilidad_%",
        size="Capital_Recuperable",
        color="Universidad",
        hover_name="Carrera_SURDAO",
        labels={
            "Desercion_SIES_pct": "Tasa de Deserción (%)",
            "Empleabilidad_%": "Empleabilidad (%)",
            "Capital_Recuperable": "Capital Recuperable ($MM)"
        },
        title="Deserción vs Empleabilidad vs Capital Recuperable"
    )
    fig_bubble.update_traces(marker=dict(opacity=0.7, line=dict(width=1, color='DarkSlateGrey')))
    fig_bubble.update_layout(
        xaxis_title="Tasa de Deserción (%)",
        yaxis_title="Empleabilidad (%)",
        legend_title="Universidad"
    )
    st.plotly_chart(fig_bubble, use_container_width=True)





