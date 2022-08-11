from matplotlib import rcParams
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
import streamlit as st

st.set_page_config(layout="wide")
st.title('CS Team KPI Report')
st.sidebar.image('./logo.png', width = 260)
st.sidebar.markdown('#')
st.sidebar.write('Fill in the form using data from the corresponding Hubspot Dashboards.')
st.sidebar.write('CES Score, Open and Overdue Tasks, Drones without Email: https://app.hubspot.com/reports-dashboard/3910549/view/3760416')
st.sidebar.write('Time to Close, Time to First Reply: https://app.hubspot.com/reports-dashboard/3910549/view/9301395')

ces_input = st.text_input('CES Score')
task_input = st.text_input('Overdue Tasks')
email_input = st.text_input('Sold Drones Without Email')
close_input = st.text_input('Time to Close (Crit 1-4)')
reply_input = st.text_input('Time to First Reply')

if st.button('Generate Report'):
    if ces_input != '' and task_input != '' and email_input != '' and close_input != '' and reply_input != '':
        ces = float(ces_input)
        task = int(task_input)
        email = int(email_input)
        close = float(close_input)
        reply = float(reply_input)
        
        fig, ax = plt.subplots(5)
        fig.set_size_inches(3.6, 5.1)
        
        ces_min = 6
        ax[0].tick_params(labelsize=5)
        if ces >= ces_min:
            ax[0].barh(1,[ces],color='#a7e1b1')
            ax[0].set_xticks(range(0,8))
            ax[0].set_yticks([])
            ax[0].set_ylabel('CES Score', size=5)
            ax[0].axvline(x=ces_min, color='k', lw=0.8, ls='--')
            ax[0].text(2.5/10,0.7, 'Goal: > 6.0', ha='left', size=6)
            ax[0].text(ces+2.5/10, 1, str(ces), va='center', ha='right', rotation=270, size=7.5, fontweight='bold')
        else:
            if ces >= 0.95*ces_min:
                ax[0].barh(1,[ces],color='lemonchiffon')
                ax[0].text(ces-1.5/10, 1, str(ces), va='center', ha='right', rotation=270, size=7.5, fontweight='bold')
            else:
                ax[0].barh(1,[ces],color='#fc8ca0')
                ax[0].text(ces+2.5/10, 1, str(ces), va='center', ha='right', rotation=270, size=7.5, fontweight='bold')
            ax[0].set_xticks(range(0,8))
            ax[0].set_yticks([])
            ax[0].set_ylabel('CES Score', size=5)
            ax[0].axvline(x=ces_min, color='k', lw=0.8, ls='--')
            ax[0].text(2.5/10,0.7, 'Goal: >= 6.0', ha='left', size=6)
            
            
        task_max = 60
        ax[1].tick_params(labelsize=5)
        if task <= task_max:
            ax[1].barh(1,[task],color='#a7e1b1')
            ax[1].set_xticks(range(0,task_max+10,int(task/10)))
            ax[1].set_yticks([])
            ax[1].set_ylabel('Overdue Tasks', size=5)
            ax[1].axvline(x=task_max, color='k', lw=0.8, ls='--')
            ax[1].text(task/34,0.7, 'Goal: <= 60 Tasks', ha='left', size=6)
            if task_max - task <= 2:
                ax[1].text(task-task/31, 1, str(task), va='center', ha='right', rotation=270, size=7.5, fontweight='bold')
            else:
                ax[1].text(task+task/31, 1, str(task), va='center', ha='right', rotation=270, size=7.5, fontweight='bold')
        else:
            if task - task_max <= 3:
                ax[1].barh(1,[task],color='#a7e1b1')
            else:
                ax[1].barh(1,[task],color='#fc8ca0')
            ax[1].set_xticks(range(0,task+10,int(task/10)))
            ax[1].set_yticks([])
            ax[1].set_ylabel('Overdue Tasks', size=5)
            ax[1].axvline(x=task_max, color='k', lw=0.8, ls='--')
            ax[1].text(task/34,0.7, 'Goal: <= 60 Tasks', ha='left', size=6)
            ax[1].text(task+task/31, 1, str(task), va='center', ha='right', rotation=270, size=7.5, fontweight='bold')
        
        email_max = 15
        ax[2].tick_params(labelsize=5)
        if email <= email_max:
            ax[2].barh(1,[email],color='#a7e1b1')
            ax[2].set_xticks(range(0,email_max+1,4))
            ax[2].set_yticks([])
            ax[2].set_ylabel('Drones w/o Email', size=5)
            ax[2].axvline(x=email_max, color='k', lw=0.8, ls='--')
            ax[2].text(email/30,0.7, 'Goal: <= 15 Drones without Email', ha='left', size=6)
            ax[2].text(email+email/30, 1, str(email), va='center', ha='right', rotation=270, size=7.5, fontweight='bold')
        else:
            if email - email_max <= 3:
                ax[2].barh(1,[email],color='#a7e1b1')
            else:
                ax[2].barh(1,[email],color='#fc8ca0')
            ax[2].set_xticks(range(0,email+1,4))
            ax[2].set_yticks([])
            ax[2].set_ylabel('Drones w/o Email', size=5)
            ax[2].axvline(x=email_max, color='k', lw=0.8, ls='--')
            ax[2].text(email/30,0.7, 'Goal: <= 15 Drones without Email', ha='left', size=6)
            ax[2].text(email+email/30, 1, str(email), va='center', ha='right', rotation=270, size=7.5, fontweight='bold')
        
        
        close_max = 35
        ax[3].tick_params(labelsize=5)
        if close <= close_max:
            ax[3].barh(1,[close],color='#a7e1b1')
            ax[3].set_xticks(range(0,close_max+1,4))
            ax[3].set_yticks([])
            ax[3].set_ylabel('Time to Close', size=5)
            ax[3].axvline(x=close_max, color='k', lw=0.8, ls='--')
            ax[3].text(close/30,0.7, 'Goal: <= 35 Days Time to Close (Crit 1-4)', ha='left', size=6)
            if close_max - close < 1:
                ax[3].text(close-close/30, 1, str(close), va='center', ha='right', rotation=270, size=7.5, fontweight='bold')
            else:
                ax[3].text(close+close/30, 1, str(close), va='center', ha='right', rotation=270, size=7.5, fontweight='bold')
        else:
            if close <= close_max*1.05:
                ax[3].barh(1,[close],color='#eeeab7')
            else:
                ax[3].barh(1,[close],color='#fc8ca0')
            ax[3].set_xticks(range(0,int(close+1),4))
            ax[3].set_yticks([])
            ax[3].set_ylabel('Time to Clos', size=5)
            ax[3].axvline(x=close_max, color='k', lw=0.8, ls='--')
            ax[3].text(close/30,0.7, 'Goal: <= 35 Days Time to Close (Crit 1-4)', ha='left', size=6)
            ax[3].text(close+close/30, 1, str(close), va='center', ha='right', rotation=270, size=7.5, fontweight='bold')
        
        ax[4].tick_params(labelsize=5)
        ax[4].barh(1,[reply],color='#a7e1b1')
        ax[4].set_xticks(range(0,25,5))
        ax[4].set_yticks([])
        ax[4].set_ylabel('Time to First Reply (h)', size=5)
        ax[4].text(reply+(reply/(reply*1.5)), 1, str(reply), va='center', ha='right', rotation=270, size=7.5, fontweight='bold')
               
        fig.tight_layout()
        
        fn = 'Friday_Report.png'
        fig.savefig(fn, dpi=500)
        st.image(fn)
        
    else:
        st.error('Please Supply All Data.')
        st.stop()
        #fig.savefig('plot.png')

st.stop()
