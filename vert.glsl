varying vec4 vertex_color;

void main()
{
    gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex;
    vertex_color = vec4(0.0,0.0,0.0,1.0);
}
