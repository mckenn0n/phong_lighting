varying vec4 vertex_color;

void main()
{
    gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex;gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex;

    vec4 tempNorm = vec4(gl_Normal, 1.0);

    tempNorm = gl_ModelViewMatrix * vec4(gl_Normal, 0.0);

    vertex_color = tempNorm;
}
