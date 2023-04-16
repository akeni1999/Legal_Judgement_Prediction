from fastapi import FastAPI
import pickle
app = FastAPI()
from typing import Optional
import joblib
from navie_model import predict, labelmap, lawinfo
knn_from_joblib = joblib.load('model.pkl')
# gnn = pickle.loads()



from pydantic import BaseModel
from typing import List, Optional


class Input(BaseModel):
	name: List[int] = []
	description: Optional[str] = None

@app.post("/demo/")
async def root(item: Input):
	print(item.name, type(item))
	input_arr = item.name
	ans=predict(knn_from_joblib,input_arr[0],input_arr[1],input_arr[2],input_arr[3])
	ans1=labelmap(ans[0])
	# predt = gnn.predict([])
	return {"message": lawinfo(ans1)}

