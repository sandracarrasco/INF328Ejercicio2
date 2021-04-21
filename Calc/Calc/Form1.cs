using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Collections;

namespace Calc
{
    public partial class Form1 : Form
    {
        int n;
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

           
        }

       

        private void button1_Click(object sender, EventArgs e)
        {
            string t = "";
            t = textBox1.Text;
            textBox1.Text= t+ (((Button)sender).Text);
            t = infija_postfija(t);
            Console.WriteLine(t);


            //d = Convert.ToInt16(((Button)sender).Text);
            //n = n * 10 + d;
            //textBox1.Text = n.ToString();
        }


        string infija_postfija(string t) {

            //string phrase = "The quick brown fox jumps over the lazy dog.";
           
            return t;
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {
            string b = "";
            b = (((TextBox)sender).Text);


        }

     
        private void calcular(object sender, EventArgs e)
        {

            string b = "";
            b = textBox1.Text;
            Stack miPila = new Stack();


            char[] delimiterChars = { ' ', ',', '.', ':', '\t' };


            string[] words = b.Split(delimiterChars);
            System.Console.WriteLine($"{words.Length} words in text:");

            foreach (var word in words)
            {
                System.Console.WriteLine(word);
                /*if (word.Equals("1") || word.Equals("2") || word.Equals("3") || word.Equals("4") || word.Equals("5") || word.Equals("6") || word.Equals("7") || word.Equals("8") || word.Equals("9"))
                {
                    miPila.Push(word);
                    Console.WriteLine("palabra"+word);
                }
                else

                {*/
                    if (word.Equals("+") || word.Equals("-") || word.Equals("*") || word.Equals("/") )
                    {
                        string op1 = "";
                        string op2 = "";
                        op2 = (string)miPila.Pop();
                        op1 = (string)miPila.Pop();

                        int x = Int32.Parse(op1);
                        int y = Int32.Parse(op2);

                        int oper = 0;

                        if (word.Equals("+"))
                        {
                            oper = x + y;
                        }
                      
                        if (word.Equals("-"))
                        {
                            oper = x - y;
                        }
                        

                        if (word.Equals("*"))
                        {
                            oper = x * y;
                        }
                               
                        if (word.Equals("/"))
                        {
                            oper = x / y;
                        }


                                 

                     


                        string numString = oper.ToString();

                        miPila.Push(numString);


                    }

                    else
                    {

                        miPila.Push(word);


                    }
                //}

            }


            String final = " ";
            if (miPila.Count != 0) {

                final = (string)miPila.Pop();


            }

            Console.WriteLine(final);

            textBox1.Text = final;



        }

        private void limpiar(object sender, EventArgs e)
        {

            textBox1.Text = "";

        }
    }
}
