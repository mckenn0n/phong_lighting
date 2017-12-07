varying vec3 norm;
varying vec3 verPos;

void main (void){
   vec3 LightDir = normalize(gl_LightSource[0].position.xyz - verPos);
   vec3 viewDir = normalize(-verPos);
   vec3 H = normalize(LightDir+viewDir);
   float Ka =  0.1;
   float Kd =  0.3;
   float Ks =  1.0;
   float N = 20.0;
   vec4 ambC = vec4(0.0, 0.0, 1.0, 1.0);
   vec4 diffC = vec4(1.0, 1.0, 1.0, 1.0);
   vec4 specC = vec4(1.0, 0.0, 0.0, 1.0); 
   vec4 amb = Ka * ambC;
   vec4 diff = Kd * diffC * max(dot(LightDir,norm), 0.0);
   diff = clamp(diff, 0.0, 1.0);
   vec4 spec = Ks * specC * pow(max(dot(H,norm),0.0),N);
   spec = clamp(spec, 0.0, 1.0);
   gl_FragColor = amb + diff + spec;
}