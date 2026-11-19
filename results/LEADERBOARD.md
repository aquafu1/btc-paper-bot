# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 3:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 844 windows, 23231 settled trades, 64 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 430 | 33.7 | 34.9 | $-317.48 | -7.4% | $682.52 | -1.2 | done | can't tell from luck |
| value_ev10 | 1061 | 37.6 | 39.1 | $-776.71 | -7.3% | $223.29 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 1959 | 50.0 | 49.7 | $-858.44 | -4.4% | $141.56 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 2372 | 50.8 | 50.6 | $-875.81 | -3.7% | $124.19 | -1.8 | done | can't tell from luck |
| trend_filter | 1368 | 49.9 | 50.9 | $-964.14 | -7.0% | $35.86 | -2.7 | done | losing for real |
| value_ev5 | 1606 | 39.8 | 41.0 | $-1069.26 | -6.7% | $-69.26 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 1959 | 50.0 | 51.1 | $-1394.02 | -7.1% | $-394.02 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 2372 | 49.2 | 50.3 | $-1461.04 | -6.2% | $-461.04 | -3.0 | done | losing for real |
| coinflip | 3368 | 50.2 | 50.3 | $-1476.16 | -4.4% | $-476.16 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 3368 | 51.2 | 51.7 | $-1617.84 | -4.8% | $-617.84 | -2.9 | done | losing for real |
| always_up | 3368 | 47.1 | 49.5 | $-3165.88 | -9.4% | $-2165.88 | -5.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5287 | 48.1 | 49.1 | $-3172.83 |
| ETH | 5784 | 48.0 | 48.5 | $-3941.37 |
| SOL | 6058 | 48.2 | 48.6 | $-3612.26 |
| XRP | 6102 | 48.5 | 48.5 | $-3250.33 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
