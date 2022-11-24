import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(layout="wide")
st.title('CS Team KPI Report')
st.sidebar.image('./logo.png', width = 260)

# Password Check

def check_password():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["password"] == st.secrets["password"]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store password
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show input for password.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("Password Incorrect.")
        return False
    else:
        # Password correct.
        return True

if check_password():
    #st.sidebar.image('./logo.png', width = 260)
    st.sidebar.markdown('#')
    st.sidebar.write('Fill in the form using data from the corresponding Hubspot Dashboards.')
    st.sidebar.write('CES Score, Time to Close: https://app.hubspot.com/reports-dashboard/3910549/view/9528821')
    st.sidebar.markdown('#')
    st.sidebar.write('Time to First Reply: https://app.hubspot.com/reports-dashboard/3910549/view/9301395')
    
    ces_overall_input = st.text_input('CES Score (Overall)')
    ces_l1_input = st.text_input('CES Score (Tier 1)')
    ces_l2_input = st.text_input('CES Score (Tier 2)')
    ces_l3_input = st.text_input('CES Score (Tier 3)')
    close_input = st.text_input('Time to Close (Crit 1-4)')
    reply_input = st.text_input('Time to First Reply')
    
    if st.button('Generate Report'):
        if ces_overall_input != '' and ces_l1_input != '' and ces_l2_input != '' and ces_l3_input != '' and close_input != '' and reply_input != '':
            ces_overall = float(ces_overall_input)
            ces_l1 = float(ces_l1_input)
            ces_l2 = float(ces_l2_input)
            ces_l3 = float(ces_l3_input)
            close = float(close_input)
            reply = float(reply_input)
            
            fig, ax = plt.subplots(6)
            fig.set_size_inches(3.6, 5.1)
            
            ces_min = 6
            ax[0].tick_params(labelsize=5)
            if ces_overall >= ces_min:
                ax[0].barh(1,[ces_overall],color='#a7e1b1')
                ax[0].set_xticks(range(0,8))
                ax[0].set_yticks([])
                ax[0].set_ylabel('CES Score (Overall)', size=5)
                ax[0].axvline(x=ces_min, color='k', lw=0.8, ls='--')
                ax[0].text(2.5/10,0.7, 'Goal: > 6.0', ha='left', size=6)
                ax[0].text(ces_overall+2.5/10, 1, str(ces_overall), va='center', ha='right', rotation=270, size=7.5, fontweight='bold')
            else:
                if ces_overall >= 0.95*ces_min:
                    ax[0].barh(1,[ces_overall],color='lemonchiffon')
                    ax[0].text(ces_overall-1.5/10, 1, str(ces_overall), va='center', ha='right', rotation=270, size=7.5, fontweight='bold')
                else:
                    ax[0].barh(1,[ces_overall],color='#fc8ca0')
                    ax[0].text(ces_overall+2.5/10, 1, str(ces_overall), va='center', ha='right', rotation=270, size=7.5, fontweight='bold')
                ax[0].set_xticks(range(0,8))
                ax[0].set_yticks([])
                ax[0].set_ylabel('CES Score (Overall)', size=5)
                ax[0].axvline(x=ces_min, color='k', lw=0.8, ls='--')
                ax[0].text(2.5/10,0.7, 'Goal: >= 6.0', ha='left', size=6)
                
            ax[1].tick_params(labelsize=5)
            if ces_l1 >= ces_min:
                ax[1].barh(1,[ces_l1],color='#a7e1b1')
                ax[1].set_xticks(range(0,8))
                ax[1].set_yticks([])
                ax[1].set_ylabel('CES Score (Tier 1)', size=5)
                ax[1].axvline(x=ces_min, color='k', lw=0.8, ls='--')
                ax[1].text(2.5/10,0.7, 'Goal: > 6.0', ha='left', size=6)
                ax[1].text(ces_l1+2.5/10, 1, str(ces_l1), va='center', ha='right', rotation=270, size=7.5, fontweight='bold')
            else:
                if ces_l1 >= 0.95*ces_min:
                    ax[1].barh(1,[ces_l1],color='lemonchiffon')
                    ax[1].text(ces_l1-1.5/10, 1, str(ces_l1), va='center', ha='right', rotation=270, size=7.5, fontweight='bold')
                else:
                    ax[1].barh(1,[ces_l1],color='#fc8ca0')
                    ax[1].text(ces_l1+2.5/10, 1, str(ces_l1), va='center', ha='right', rotation=270, size=7.5, fontweight='bold')
                ax[1].set_xticks(range(0,8))
                ax[1].set_yticks([])
                ax[1].set_ylabel('CES Score (Tier 1)', size=5)
                ax[1].axvline(x=ces_min, color='k', lw=0.8, ls='--')
                ax[1].text(2.5/10,0.7, 'Goal: >= 6.0', ha='left', size=6)

            ax[2].tick_params(labelsize=5)
            if ces_l2 >= ces_min:
                ax[2].barh(1,[ces_l2],color='#a7e1b1')
                ax[2].set_xticks(range(0,8))
                ax[2].set_yticks([])
                ax[2].set_ylabel('CES Score (Tier 2)', size=5)
                ax[2].axvline(x=ces_min, color='k', lw=0.8, ls='--')
                ax[2].text(2.5/10,0.7, 'Goal: > 6.0', ha='left', size=6)
                ax[2].text(ces_l2+2.5/10, 1, str(ces_l2), va='center', ha='right', rotation=270, size=7.5, fontweight='bold')
            else:
                if ces_l2 >= 0.95*ces_min:
                    ax[2].barh(1,[ces_l2],color='lemonchiffon')
                    ax[2].text(ces_l2-1.5/10, 1, str(ces_l2), va='center', ha='right', rotation=270, size=7.5, fontweight='bold')
                else:
                    ax[2].barh(1,[ces_l2],color='#fc8ca0')
                    ax[2].text(ces_l2+2.5/10, 1, str(ces_l2), va='center', ha='right', rotation=270, size=7.5, fontweight='bold')
                ax[2].set_xticks(range(0,8))
                ax[2].set_yticks([])
                ax[2].set_ylabel('CES Score (Tier 2)', size=5)
                ax[2].axvline(x=ces_min, color='k', lw=0.8, ls='--')
                ax[2].text(2.5/10,0.7, 'Goal: >= 6.0', ha='left', size=6)                

            ax[3].tick_params(labelsize=5)
            if ces_l3 >= ces_min:
                ax[3].barh(1,[ces_l3],color='#a7e1b1')
                ax[3].set_xticks(range(0,8))
                ax[3].set_yticks([])
                ax[3].set_ylabel('CES Score (Tier 3)', size=5)
                ax[3].axvline(x=ces_min, color='k', lw=0.8, ls='--')
                ax[3].text(2.5/10,0.7, 'Goal: > 6.0', ha='left', size=6)
                ax[3].text(ces_l3+2.5/10, 1, str(ces_l3), va='center', ha='right', rotation=270, size=7.5, fontweight='bold')
            else:
                if ces_l3 >= 0.95*ces_min:
                    ax[3].barh(1,[ces_l3],color='lemonchiffon')
                    ax[3].text(ces_l3-1.5/10, 1, str(ces_l3), va='center', ha='right', rotation=270, size=7.5, fontweight='bold')
                else:
                    ax[3].barh(1,[ces_l3],color='#fc8ca0')
                    ax[3].text(ces_l3+2.5/10, 1, str(ces_l3), va='center', ha='right', rotation=270, size=7.5, fontweight='bold')
                ax[3].set_xticks(range(0,8))
                ax[3].set_yticks([])
                ax[3].set_ylabel('CES Score (Tier 3)', size=5)
                ax[3].axvline(x=ces_min, color='k', lw=0.8, ls='--')
                ax[3].text(2.5/10,0.7, 'Goal: >= 6.0', ha='left', size=6)                  
                      
            close_max = 35
            ax[4].tick_params(labelsize=5)
            if close <= close_max:
                ax[4].barh(1,[close],color='#a7e1b1')
                ax[4].set_xticks(range(0,close_max+1,4))
                ax[4].set_yticks([])
                ax[4].set_ylabel('Time to Close', size=5)
                ax[4].axvline(x=close_max, color='k', lw=0.8, ls='--')
                ax[4].text(close/30,0.7, 'Goal: <= 35 Days Time to Close (Crit 1-4)', ha='left', size=6)
                if close_max - close < 1:
                    ax[4].text(close-close/30, 1, str(close), va='center', ha='right', rotation=270, size=7.5, fontweight='bold')
                else:
                    ax[4].text(close+close/30, 1, str(close), va='center', ha='right', rotation=270, size=7.5, fontweight='bold')
            else:
                if close <= close_max*1.05:
                    ax[4].barh(1,[close],color='#eeeab7')
                else:
                    ax[4].barh(1,[close],color='#fc8ca0')
                ax[4].set_xticks(range(0,int(close+1),4))
                ax[4].set_yticks([])
                ax[4].set_ylabel('Time to Close', size=5)
                ax[4].axvline(x=close_max, color='k', lw=0.8, ls='--')
                ax[4].text(close/30,0.7, 'Goal: <= 35 Days Time to Close (Crit 1-4)', ha='left', size=6)
                ax[4].text(close+close/30, 1, str(close), va='center', ha='right', rotation=270, size=7.5, fontweight='bold')
            
            ax[5].tick_params(labelsize=5)
            ax[5].barh(1,[reply],color='#a7e1b1')
            ax[5].set_xticks(range(0,25,5))
            ax[5].set_yticks([])
            ax[5].set_ylabel('Time to First Reply (h)', size=5)
            ax[5].text(reply+(reply/(reply*1.5)), 1, str(reply), va='center', ha='right', rotation=270, size=7.5, fontweight='bold')
                   
            fig.tight_layout()
            
            fn = 'Friday_Report.png'
            fig.savefig(fn, dpi=500)
            st.image(fn)
            
        else:
            st.error('Please Supply All Data.')
            st.stop()
            #fig.savefig('plot.png')
    
    st.stop()
