from flask import Flask, jsonify
from pytrends.request import TrendReq

app = Flask(__name__)

@app.route('/trending-seo-topics', methods=['GET'])
def get_trending_seo_topics():
    pytrends = TrendReq(hl='en-US', tz=360)
    keywords = ["SEO", "Digital Marketing", "Google Algorithm", "Backlinks", "Content Marketing"]
    pytrends.build_payload(keywords, cat=0, timeframe='now 7-d', geo='US', gprop='')
    
    related_queries = pytrends.related_queries()
    trending_keywords = related_queries.get("SEO", {}).get("rising", None)

    if trending_keywords is not None:
        return jsonify({"Trending SEO Topics": trending_keywords.to_dict()})
    else:
        return jsonify({"message": "No trending data available."})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
