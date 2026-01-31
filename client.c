#include <stdio.h>
#include <unistd.h>
#include <arpa/inet.h>

int main() {
    int sockfd = socket(AF_INET, SOCK_STREAM, 0);

    struct sockaddr_in addr;
    addr.sin_family = AF_INET;
    addr.sin_port = htons(8080);
    addr.sin_addr.s_addr = inet_addr("127.0.0.1");

    connect(sockfd, (struct sockaddr*)&addr, sizeof(addr));

    char buffer[1024];
    recv(sockfd, buffer, sizeof(buffer), 0);
    printf("Received: %s", buffer);

    close(sockfd);
    return 0;
}
