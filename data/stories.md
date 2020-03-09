## say goodbye
* goodbye
  - utter_goodbye
## interactive_story_1
* weather
    - utter_weather
* currency
    - utter_currency
* currency
    - utter_currency
* zodiac
    - utter_zodiac
* tell_me_a_joke
    - utter_tell_me_a_joke
* harassment
    - utter_harassment
* harassment
    - utter_harassment

## out of scope
* out_of_scope
   - utter_default
* out_of_scope
   - utter_default
* out_of_scope
   - utter_help_message
  
## info_about_service_centers
 * info_about_service_centers
   - info_about_service_centers_form
   - form{"name": "info_about_service_centers_form"}
   
## hello+sevice_centers
 * hello
   - utter_hello
 * info_about_service_centers
   - info_about_service_centers_form
   - form{"name": "info_about_service_centers_form"}

## hello+sevice_centers
 * hello
   - utter_hello
 * currency
   - utter_currency
 * info_about_service_centers
   - info_about_service_centers_form
   - form{"name": "info_about_service_centers_form"}

   
## interactive_story_1
* hello
    - utter_hello
* zodiac
    - utter_zodiac
* info_about_service_centers
    - info_about_service_centers_form
    - form{"name": "info_about_service_centers_form"}
    - slot{"requested_slot": "city"}
* form: info_about_service_centers{"city": "ბათუმი"}
    - slot{"city": "ბათუმი"}
    - form: info_about_service_centers_form
    - slot{"city": "ბათუმი"}
    - slot{"requested_slot": "direction"}
* weather
    - utter_weather
* what_can_you_do
    - utter_what_can_you_do
* info_about_service_centers
    - utter_ask_direction

## interactive_story_1
* hello
    - utter_hello
* info_about_service_centers
    - info_about_service_centers_form
    - form{"name": "info_about_service_centers_form"}
    - slot{"requested_slot": "city"}
* form: info_about_service_centers{"city": "ბათუმში"}
    - slot{"city": "ბათუმში"}
    - form: info_about_service_centers_form
    - slot{"city": "ბათუმში"}
    - slot{"requested_slot": "direction"}
* form: info_about_service_centers{"direction": "რითეილი"}
    - slot{"direction": "რითეილი"}
    - form: info_about_service_centers_form
    - slot{"direction": "რითეილი"}
    - form{"name": null}
    - slot{"requested_slot": null}
* currency
    - utter_currency
* harassment
    - utter_harassment
* zodiac
    - utter_zodiac
* tell_me_a_joke
    - utter_tell_me_a_joke
* tell_me_a_joke
    - utter_tell_me_a_joke
    
    
 ## savings
 
 * info_about_savings
    - utter_info_about_savings_1
    - utter_info_about_savings_2
    - utter_hope_i_helped

 ## loans_happy_path
 
 * hello
   - utter_hello
 * info_about_loans
   - info_about_loans_form
   - form{"name": "info_about_loans_form"}
 
 ## feedback
 
 * thanks
    - utter_feedback   

## interactive_story_1
* what_can_you_do
    - utter_what_can_you_do
* info_about_loans{"loan": "სესხები"}
    - slot{"loan": "სესხები"}
    - info_about_loans_form
    - form{"name": "info_about_loans_form"}
    - slot{"requested_slot": "loan_type"}
* form: info_about_loans{"loan_type": "ავტო"}
    - slot{"loan_type": "ავტო"}
    - form: info_about_loans_form
    - slot{"loan_type": "ავტო"}
    - slot{"requested_slot": "initial_amount"}
* form: info_about_loans{"initial_amount": "1000"}
    - slot{"initial_amount": "1000"}
    - form: info_about_loans_form
    - slot{"initial_amount": "1000"}
    - slot{"loan_type": null}
    - slot{"initial_amount": null}
    - form{"name": null}
    - slot{"requested_slot": null}
* thanks
    - utter_feedback