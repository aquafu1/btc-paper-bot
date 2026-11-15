# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 9:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 389 windows, 10625 settled trades, 71 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 196 | 37.2 | 36.6 | $-26.95 | -1.4% | $973.05 | -0.1 | Sat 11:15 PM | too few trades (196/200) |
| value_ev10 | 507 | 40.0 | 40.5 | $-209.23 | -4.1% | $790.77 | -0.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 897 | 50.5 | 49.8 | $-253.30 | -2.8% | $746.70 | -0.9 | done | can't tell from luck |
| value_ev5 | 748 | 41.7 | 42.1 | $-328.33 | -4.4% | $671.67 | -1.0 | done | can't tell from luck |
| trend_filter | 600 | 49.5 | 50.5 | $-365.75 | -6.1% | $634.25 | -1.5 | done | can't tell from luck |
| momentum_15m_0.10pct | 1068 | 49.3 | 49.7 | $-463.55 | -4.3% | $536.45 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 1068 | 50.7 | 52.1 | $-714.18 | -6.7% | $285.82 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 897 | 49.5 | 52.1 | $-788.17 | -8.8% | $211.83 | -2.8 | done | losing for real |
| coinflip | 1548 | 49.8 | 50.8 | $-866.57 | -5.6% | $133.43 | -2.2 | done | losing for real |
| momentum_5m_0.00pct | 1548 | 49.7 | 51.5 | $-1067.83 | -6.9% | $-67.83 | -2.8 | done | losing for real |
| always_up | 1548 | 46.2 | 50.7 | $-1920.16 | -12.4% | $-920.16 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2402 | 47.7 | 49.4 | $-1688.21 |
| ETH | 2669 | 47.8 | 48.9 | $-1778.71 |
| SOL | 2750 | 48.0 | 49.5 | $-2056.28 |
| XRP | 2804 | 48.7 | 49.2 | $-1480.81 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
