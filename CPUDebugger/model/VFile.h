#ifndef VFILE_H
#define VFILE_H
#include "FFile.h"
class VFile: public FFile {
public:
    VFile(QFile*);
    void Show();
};

#endif // VFILE_H
