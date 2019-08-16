// Options:   --max-funcs 1 --no-argc --concise -o ./.csmith/delay_1.c
#include "csmith.h"

extern int global1;
extern int global2;
void change_global(int val)
{
    global2 = val;
}

static long __undefined;



static int32_t g_3[8][9][3] = {{{0x5C74600EL,0L,0x3BE7680DL},{0x76492A41L,0x3387DD7DL,0x090D790FL},{(-1L),(-1L),0x64C7B7F6L},{0xCC321A07L,0L,0xFB18BA70L},{2L,0xD0E72EE7L,(-3L)},{(-1L),0x3518F4C6L,0x5F5C9B8DL},{1L,0x3D2AFDDFL,(-2L)},{0x3518F4C6L,0x4FFDEABFL,1L},{(-10L),0x2FB29D94L,(-9L)}},{{2L,(-9L),6L},{3L,0xE45D764CL,0xCFADBACDL},{(-1L),0x4BDAC842L,(-1L)},{0x2C5D177CL,0x3BE7680DL,(-2L)},{1L,2L,0x20B50F6BL},{0x0AD8EA5FL,9L,3L},{(-1L),(-3L),0x4C266D8FL},{0xA4182467L,1L,(-1L)},{0x64C7B7F6L,0x0A0CD95FL,1L}},{{0xE45D764CL,0xBCE8D550L,1L},{(-1L),0L,0x3387DD7DL},{0L,0xCFADBACDL,0L},{1L,0xE45D764CL,6L},{0x3387DD7DL,0x76492A41L,0x85EA6EDAL},{0xCFADBACDL,0L,1L},{0x4C90EB1FL,0x498B94BEL,0L},{(-1L),(-1L),0xAC46DDCDL},{2L,0x52B8909FL,0x090D790FL}},{{0L,(-1L),(-1L)},{0xADC9FE9AL,1L,(-1L)},{0L,3L,0xBA4AEFC5L},{0x8F82EA91L,(-1L),0xE45D764CL},{0L,0xD0E72EE7L,7L},{0x2C5D177CL,(-1L),(-1L)},{0x837DEF5FL,3L,0x9D73DF2EL},{0x2FB29D94L,1L,(-9L)},{1L,(-1L),(-1L)}},{{0x4FFDEABFL,0x52B8909FL,1L},{2L,(-1L),0xDBD8D46CL},{6L,0x498B94BEL,0xCFADBACDL},{0x5C74600EL,0L,0xBCE8D550L},{(-3L),0x76492A41L,0x52B8909FL},{0L,0xE45D764CL,0x3439FCB6L},{(-1L),0xCFADBACDL,6L},{0x4E719BA7L,0L,0x3D2AFDDFL},{0x6652D0DAL,0xBCE8D550L,0x34AAFBEBL}},{{0x8FE7528AL,0x0A0CD95FL,0x9B2B534DL},{0x9D73DF2EL,1L,(-2L)},{0x20B50F6BL,(-3L),0xCAE8EF33L},{0x20B50F6BL,0xADC9FE9AL,0x8FE7528AL},{0x9D73DF2EL,(-9L),2L},{0x8FE7528AL,0xBA4AEFC5L,1L},{0x6652D0DAL,0x8FE7528AL,0xA4182467L},{0x4E719BA7L,1L,2L},{(-1L),6L,0x76492A41L}},{{0L,0x3518F4C6L,(-3L)},{(-3L),0x2FB29D94L,9L},{0x5C74600EL,0xCAE8EF33L,0x195C588CL},{6L,0x5F5C9B8DL,(-3L)},{2L,0x79FACD4AL,0x20B50F6BL},{0x4FFDEABFL,0x9D73DF2EL,0x5F5C9B8DL},{1L,1L,1L},{0x2FB29D94L,(-1L),(-9L)},{0x837DEF5FL,(-10L),1L}},{{0x2C5D177CL,0x4C266D8FL,0x5C74600EL},{0L,0x837DEF5FL,1L},{0x8F82EA91L,0x090D790FL,(-9L)},{0L,(-10L),1L},{0xADC9FE9AL,7L,0x5F5C9B8DL},{0L,0x0AD8EA5FL,0x20B50F6BL},{2L,(-1L),(-3L)},{(-1L),1L,0x195C588CL},{0x4C90EB1FL,0L,9L}}};
static int32_t *g_12 = &g_3[5][6][0];
static int32_t ** volatile g_11 = &g_12;



static uint32_t  func_1(void);




static uint32_t  func_1(void)
{ 
    int32_t *l_2 = &g_3[5][6][0];
    uint8_t l_4 = 255UL;
    int32_t *l_7[1];
    uint16_t l_8 = 65530UL;
    int i;
    for (i = 0; i < 1; i++)
        l_7[i] = &g_3[6][4][1];
    ++l_4;
    l_8++;
    (*g_11) = l_7[0];
    return g_3[4][7][0];
}





int slp (int print_hash_value)
{
    int i, j, k;
    platform_main_begin();
    crc32_gentab();
    func_1();
    for (i = 0; i < 8; i++)
    {
        for (j = 0; j < 9; j++)
        {
            for (k = 0; k < 3; k++)
            {
                transparent_crc(g_3[i][j][k], "g_3[i][j][k]", print_hash_value);
                if (print_hash_value) printf("index = [%d][%d][%d]\n", i, j, k);

            }
        }
    }
    platform_main_end(crc32_context ^ 0xFFFFFFFFUL, print_hash_value);
    return 0;
}
