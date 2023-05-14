#include <gtest/gtest.h>
#include <gmock/gmock-matchers.h>
#include "Controllers/PreDebugController.h"

using namespace testing;

QString file_path = "test.asm";
QString new_file_path = "test2.asm";
QString out_file = "result.txt";

// 是否可以正常编译
TEST(work_test, case1)
{
    PreDebugController::uploadFile(file_path);
    ASSERT_FALSE(PreDebugController::getFile() == nullptr);
    PreDebugController::compileAsm();
    ASSERT_FALSE(PreDebugController::getAsm() == nullptr);
}

// 上传文件后clear，进行编译是否可以正常抛出异常
TEST(null_compiler_test, case1)
{
    PreDebugController::uploadFile(file_path);
    PreDebugController::clear();
    EXPECT_THROW(PreDebugController::compileAsm(), std::invalid_argument);
}


// 检查输出的QByteArray
TEST(correction_test, case1)
{
    PreDebugController::uploadFile(file_path);
    PreDebugController::compileAsm();
    QByteArray byteArray = PreDebugController::getAsm()->getBin();
    ASSERT_FALSE(byteArray == nullptr);
    QFile file(out_file);
    qDebug() << byteArray.toHex();
    if (file.open(QIODevice::WriteOnly))
    {
        // 将 QByteArray 内容写入文件
        file.write(byteArray);
        // 关闭文件
        file.close();
    }
}