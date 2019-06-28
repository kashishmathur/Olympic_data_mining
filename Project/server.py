# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 12:50:52 2019

@author: HP
"""

from flask import Flask, request, render_template, url_for,Markup
from new_project import *


app = Flask(__name__)


@app.route("/main")
def home():
    return render_template("main.html")

@app.route("/about")
def abt():
    return render_template("about.html")

@app.route("/visualizations")
def vis():
    return render_template("visualizations.html")

@app.route("/visualizations/medals")
def med():
    return render_template("medals.html")
    

@app.route("/visualizations/graph1")
def graph1():
    result = Athlt_pc_yr()
    return render_template("graph.html",div_placeholder1=Markup(result[0]),div_placeholder2=Markup(result[1]))
   

@app.route("/visualizations/graph2")
def graph2():
    result = athlt_pc_gn_yr()
    return render_template("graph.html",div_placeholder1=Markup(result[0]),div_placeholder2=Markup(result[1]))

@app.route("/visualizations/graph3")
def graph3():
    result = gn_ditb_gm()
    return render_template("graph.html",div_placeholder1=Markup(result[0]),div_placeholder2=Markup(result[1]))

@app.route("/visualizations/graph4")
def graph4():
    result = cntry_pc_gm()
    return render_template("graph.html",div_placeholder1=Markup(result[0]),div_placeholder2=Markup(result[1]))

@app.route("/visualizations/graph5")
def graph5():
    result = hst_pc_nt()
    return render_template("graph.html",div_placeholder1=Markup(result))

@app.route("/visualizations/graph6")
def graph6():
    result = hst_host_cnty()
    return render_template("graph.html",div_placeholder1=Markup(result[0]),div_placeholder2=Markup(result[1]))

@app.route("/visualizations/graph7")
def graph7():
    result = hst_host_city()
    return render_template("graph.html", div_placeholder1=Markup(result))

@app.route("/visualizations/graph8")
def graph8():
    result = avg_AHV()
    return render_template("graph.html", div_placeholder1=Markup(result[0]),div_placeholder2=Markup(result[1]))

@app.route("/visualizations/graph9")
def graph9():
    result = uniq_spt_yr()
    return render_template("graph.html",div_placeholder1=Markup(result[0]), div_placeholder2=Markup(result[1]))

@app.route("/visualizations/graph10")
def graph10():
    result = event_rto_gn()
    return render_template("graph.html",div_placeholder1=Markup(result[0]),div_placeholder2=Markup(result[1]))

@app.route("/visualizations/graph11")
def graph11():
    result = event_gn_yr()
    return render_template("graph.html",div_placeholder1=Markup(result[0]),div_placeholder2=Markup(result[1]))

@app.route("/visualizations/graph13")
def graph13():
    result = smr_revenue_cat()
    return render_template("graph.html", div_placeholder1=Markup(result))

@app.route("/visualizations/graph14")
def graph14():
    result = won_mdl_ech_ctg()
    return render_template("graph.html", div_placeholder1=Markup(result))

@app.route("/visualizations/graph15")
def graph15():
    result = rslt_mdl_ech_spt_ctg()
    return render_template("graph.html", div_placeholder1=Markup(result))

@app.route("/visualizations/graph16")
def graph16():
    result = top_10_athlt()
    return render_template("graph.html",div_placeholder1=Markup(result[0]),div_placeholder2=Markup(result[1]),div_placeholder3=Markup(result[2]))

if __name__ == "__main__":
    app.run()
    
