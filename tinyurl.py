"""
TinyURL plugin

Copyright (C) 2015 Sindastra <https://github.com/sindastra>

The above copyright notice and this notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

from cloudbot import hook
import re
import urllib.parse
import urllib.request

@hook.command("tiny","tinyurl")
def tiny(text):
	m = re.search("https?://[a-zA-Z0-9-\.]+[a-zA-Z\.]+[a-zA-Z0-9-\._~:/\?#\[\]@!$&'\(\)\*\+,;=]+", text)
	if not m:
		return "Invalid URL.";
	else:
		url = urllib.parse.quote_plus(text)
		return urllib.request.urlopen( "http://tinyurl.com/api-create.php?url=" + url ).read(64).decode()