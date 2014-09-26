//Builds from OpenSCAD: The Programmers Solid 3D CAD Modeller
//Caesar Cipher 3D Tool
use <MCAD/fonts.scad>

thisFont=8bit_polyfont();
x_shift=thisFont[0][0];
y_shift=thisFont[0][1];

letters=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"];

module circle_words(word_offset=20.0,word_height=52.0) {
  for(i=[0:(len(letters)-1)]) assign( hourHandAngle=(i+1)*360/len(letters), theseIndicies=search(letters[i],thisFont[2],1,1) ) {
    rotate(hourHandAngle) translate([word_offset,0])
      for( j=[0:(len(theseIndicies)-1)] ) translate([j*x_shift,-y_shift/2]) {
        rotate(90) linear_extrude(height=word_height) polygon(points=thisFont[2][theseIndicies[j]][6][0],paths=thisFont[2][theseIndicies[j]][6][1]);
      }
  }
}

translate([100,100,0])
color([255/255,192/255,32/255])
{
  circle_words(word_offset=38.0,word_height=5.0);
  cylinder(h = 10, r1 = 20, r2 = 10,d2=25, center = false);
  cylinder(h = 5, r = 39.5, center = true, $fn = 100);
  rotate_extrude(convexity = 10) translate([39, 2, 0]) circle(r = 1, $fn = 100);
  rotate_extrude(convexity = 10) translate([29, 2, 0]) circle(r = 1, $fn = 100);
}
color([18/255,56/255,131/255])
{
  circle_words(word_offset=50.0,word_height=5.0);
  translate([0,0,-5]) cylinder(h = 5, r = 55, center = true, $fn = 100);

  difference() {
    cylinder (h = 5,r=55, center = true, $fn=100);
    cylinder (h = 6, r=40, center = true, $fn=100);
  }

  rotate_extrude(convexity = 10) translate([55, 2, 0]) circle(r = 1, $fn = 100);
}
