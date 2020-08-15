import flask
from model.model import check_movie, get_recommendations,all_movies

app = flask.Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def main():

    no_of_recommendation = 5

    if flask.request.method == 'GET':
        return(flask.render_template('index.html',movie_list=all_movies))

    if flask.request.method == 'POST':
        m_name = flask.request.form['movie_name'].lower()
        if not check_movie(m_name):
            return(flask.render_template('notfound.html',name=m_name))
        else:
            names = get_recommendations(m_name, no_of_recommendation)
            return flask.render_template('found.html',movie_names=names)


if __name__ == '__main__':
    app.run()
