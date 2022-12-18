from flask import Flask, Response, request
from siritori import Siritori, FlagType

app = Flask(__name__)
siritori = Siritori("output.txt")

@app.route("/siritori", methods=['POST'])
def index():
  global siritori
  data = request.get_json()
  text = data["noun"]
  next_noun, type = siritori.return_nextnoun(text)
  if type is FlagType.USER_WIN.value:
    next_noun + "\nあなたの勝ちです"
  elif type is FlagType.USER_LOSE.value:
      next_noun + "\nあなたの負けです"
  return Response(response=next_noun, status=200)

@app.route("/init", methods=["GET"])
def init():
  global siritori
  siritori = Siritori("output.txt")
  return Response(response="しりとり" ,status=200)

if __name__ == "__main__":
  app.debug = True
  app.run(host="0.0.0.0", port=5000)