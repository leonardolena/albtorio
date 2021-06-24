class ExamException(Exception):
    pass
class CSVTimeSeriesFile:

    def __init__ (self,name):
         self.name=name

    def get_data(self):
        timeseries=[]
        try:
            file=open(self.name,'r')
        except:
            raise ExamException('problemi apertura file')
        for line in file :
            element = line.split(",")
            
            if element[0] != 'epoch': 
                epoch=element[0]
                temp=element[1]
                try:
                    epoch=round(float(epoch))
                    temp=float(temp)
                except:
                    del element
                if epoch==0 or temp==0:
                    raise ExamException('dato mancante')
                    continue   
                
                timeseries.append([epoch,temp])
            
        return timeseries


def compute_daily_variance(time_series):
    dv=0
    varlist=[]
    itemlist=[]
    for item in time_series:   
        
        if (item[0]&864001!=0):  
            itemlist.append(item[1])
        elif(len(itemlist)==0):
            itemlist.append(item[1])
        else:  
            somma=itemlist[0]    
            media=0
            var=0
            i=1
            while i<len(itemlist):
                somma+=itemlist[i]
                media=somma/(i+1)
                var+=(itemlist[i]-media)**2
                i+=1
            dv= var/len(itemlist)
            del itemlist[:]
            itemlist.append(item[1])
            varlist.append(dv)
    return varlist




time_series_file = CSVTimeSeriesFile(name='data.csv')
time_series= time_series_file.get_data()
print(compute_daily_variance(time_series))

