import streamlit as st

from converter import RomanNumeralConverter

st.title('Roman Numeral Converter')

converter = RomanNumeralConverter()

notation = {'Arabic to Roman': converter.int_to_roman, 'Roman to Arabic': converter.roman_to_int}

selected_notation = st.selectbox('Choose notation', list(notation))

if selected_notation == 'Arabic to Roman':
    arabic_number = st.number_input('Enter an Arabic number', min_value=1, value=1)
    result = notation[selected_notation](arabic_number)
    st.success(result)
else:
    roman_string = st.text_input('Enter a Roman numeral', max_chars=15, value='I')
    if roman_string:
        try:
            result = notation[selected_notation](roman_string)
            st.success(result)
        except ValueError:
            st.error('Invalid Roman numeral entered!')
