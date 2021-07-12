if (isset($_POST(['submit'])))  #check userinput
{
  $mailto ="yonella.skilly@younglings.africa";
  $from = $_POST['email']
  $name = $_POST['name']
  $subject = $_POST['subject']
  $subject = $_POST = "Your massage submitted successfully | HMA webDesign ";
  $massage ="Client Name: " &name. "wrote the following massage"."/n/n".$_POST['MASSAGE'];
  $massage2 = "Dear". $name. "Thank you for contacting me, I will get back to you";
  $headers = "From: ".$from; //user's email
  $headers2 = "From: ".$emailto; 
  $result = mail($mailto,$subject,$massage,$headers)//Send email to the website
  $result = mail($from,$subject2,$massage2,$headers2) //send email to the user
  if($result){
      echo 'script type ="text/javascript">alert("Massage sent")'
  } else {
    echo 'script type ="text/javascript">alert("Massage not sent")'

  }

} 


?>
