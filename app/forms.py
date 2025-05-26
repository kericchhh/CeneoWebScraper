from wtforms import Form,StringField, SubmitField, validators

class ExtractForm(Form):
    product_id = StringField('Product_id',name='product_id',id='product_id',validators=[
        validators.DataRequired(message="Product id is required"),
        validators.Length(min=6,max=10,message="Product id should have between 6 and 10 characters"),
        validators.Regexp(regexp='[0-9]+$',message="Product idd can contain ony digits")
    ])
    submit = SubmitField('Extract opinions')