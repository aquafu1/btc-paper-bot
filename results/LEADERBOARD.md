# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 3:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 367 windows, 9917 settled trades, 64 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 189 | 38.1 | 36.4 | $+15.78 | +0.8% | $1015.78 | +0.1 | Sat 9:15 PM | too few trades (189/200) |
| value_ev10 | 481 | 41.4 | 40.4 | $-46.39 | -1.0% | $953.61 | -0.2 | done | can't tell from luck |
| value_ev5 | 711 | 42.6 | 42.1 | $-166.26 | -2.3% | $833.74 | -0.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 817 | 49.4 | 49.7 | $-389.36 | -4.8% | $610.64 | -1.4 | done | can't tell from luck |
| trend_filter | 552 | 48.7 | 50.5 | $-423.22 | -7.7% | $576.78 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 985 | 51.6 | 52.1 | $-488.91 | -5.0% | $511.09 | -1.6 | done | can't tell from luck |
| reversal_60m_0.30pct | 817 | 50.6 | 52.1 | $-544.41 | -6.7% | $455.59 | -2.0 | done | can't tell from luck |
| momentum_15m_0.10pct | 985 | 48.4 | 49.6 | $-576.80 | -5.9% | $423.20 | -1.8 | done | can't tell from luck |
| coinflip | 1460 | 49.9 | 50.8 | $-772.43 | -5.3% | $227.57 | -2.1 | done | losing for real |
| momentum_5m_0.00pct | 1460 | 49.5 | 51.6 | $-1084.76 | -7.4% | $-84.76 | -2.9 | done | losing for real |
| always_up | 1460 | 45.7 | 50.7 | $-1954.71 | -13.4% | $-954.71 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2228 | 47.3 | 49.3 | $-1751.00 |
| ETH | 2494 | 47.8 | 48.8 | $-1709.45 |
| SOL | 2570 | 48.1 | 49.4 | $-1752.62 |
| XRP | 2625 | 48.8 | 49.1 | $-1218.41 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
