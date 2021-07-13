from flask import Flask, request, render_template
import crawler_jobSearch as cj

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def search():
    if request.method == 'GET':
        outStr = """
        <html>
            <head>
                <title>job search</title>
            </head>
            <body>
                <h1><font face="fantasy" color="#4F4FFF">Let's start to search jobs!</font></h1>
                <form action="/" method="post">
                      <h2><font face="monospace" color="#00D1D1">Which website do you want to use?</font></h2>
                      <select name="web" style="font-size:25px;">
                          <option value="cakeresume">cakeresume</option>
                          <option value="104">104</option>
                          <option value="1111">1111</option>
                      </select>
                      <br>
                      <h2><font face="monospace" color="#00D1D1">Please enter the keyword:</font></h2>
                          <input type="textbox" name="keyword">
                      <br>
                      <h2><font face="monospace" color="#00D1D1">Please enter the end page:</font></h2>
                          <input type="textbox" name="end_page">
                      <br>
                      <br>
                      <button type="submit" style="width:120px;height:40px;font-size:20px;">Submit</button>
                </form>
            </body>
        </html>
        """
        return outStr
    elif request.method == 'POST':
        web = str(request.form.get('web'))
        keyword = str(request.form.get('keyword'))
        end_page = int(request.form.get('end_page'))
        cj.main(web, keyword, end_page)
        cj.crawler_jobSearch(web)
        df = cj.df
        return render_template('result.html', column_names=df.columns.values, row_data=list(df.values.tolist()), zip=zip)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
