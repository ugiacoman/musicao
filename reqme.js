// Host: freesummarizer.com
// User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:35.0) Gecko/20100101 Firefox/35.0
// Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
// Accept-Language: en-US,en;q=0.5
// Accept-Encoding: gzip, deflate
// Referer: http://freesummarizer.com/
// Cookie: _jsuid=777245265; _ga=GA1.2.164138903.1423973625; __smToken=elPdHJINsP5LvAYhia6OAA68; __smListBuilderShown=true; _first_pageview=1; _gat=1; _eventqueue=%7B%22heatmap%22%3A%5B%7B%22type%22%3A%22heatmap%22%2C%22href%22%3A%22%252F%22%2C%22x%22%3A324%2C%22y%22%3A1800%2C%22w%22%3A640%7D%5D%2C%22events%22%3A%5B%5D%7D; PHPSESSID=28b0843d49700e134530fbe32ea62923; __smSmartbarShown=true
// Connection: keep-alive
// Content-Type: application/x-www-form-urlencoded
// Content-Length: 6044


var http = new XMLHttpRequest();
var url = "http://www.freesummarizer.com";
var params = "text=HEREWEGOWITHSAMPLETEXT&maxsentences=1";
http.open("POST", url, true);

//Send the proper header information along with the request
http.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
http.setRequestHeader("Content-length", params.length);
http.setRequestHeader("Connection", "keep-alive");

http.onreadystatechange = function() {//Call a function when the state changes.
    if(http.readyState == 4 && http.status == 200) {
        alert(http.responseText);
    }
}
http.send(params);