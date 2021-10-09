# finding the best threshold for a machine learning model

def to_labels(model_prob,threshold):  
    return (model_prob >=threshold).astype('int')                              #model




def find_threshold(classifier,x_test,y_test,score):                            #classifier is the algorithm for predicting the model output
    probability=classifier.predict_proba(x_test)[:,1]                          # x_test is the testing set in data after splitting
    
    thresholds=np.arange(0,1,0.0001)                                            # threshold is between 0 and 1
    scores=[score(y_test,to_labels(probability,threshold))for threshold in thresholds]  #y_test is the target set in data after splitting
    highest_score=np.argmax(scores)
    print('score=%.5f'%(scores[highest_score]))
    best_threshold=threshold[highest_score]
    return (best_threshold)

probs=classifier.predict_proba(x_test)[:,1] 
def thresh(probs,best_threshold):    
    probs[probs>best_threshold]=1      # probability conversion into value of (0,1)
    probs[probs<=best_threshold]=0
    return (probs)
