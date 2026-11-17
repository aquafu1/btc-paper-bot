# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 8:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 577 windows, 15979 settled trades, 45 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1358 | 51.2 | 49.7 | $-248.07 | -1.8% | $751.93 | -0.7 | done | can't tell from luck |
| value_ev20 | 310 | 33.5 | 35.2 | $-314.56 | -10.1% | $685.44 | -1.4 | done | can't tell from luck |
| trend_filter | 927 | 50.5 | 51.0 | $-504.64 | -5.4% | $495.36 | -1.7 | done | can't tell from luck |
| value_ev10 | 749 | 37.7 | 39.4 | $-677.94 | -9.1% | $322.06 | -2.1 | done | losing for real |
| reversal_15m_0.10pct | 1625 | 51.1 | 51.0 | $-723.41 | -4.5% | $276.59 | -1.8 | done | can't tell from luck |
| value_ev5 | 1121 | 40.1 | 41.3 | $-823.91 | -7.3% | $176.09 | -2.1 | done | losing for real |
| momentum_15m_0.10pct | 1625 | 48.9 | 49.9 | $-1014.23 | -6.2% | $-14.23 | -2.5 | done | losing for real |
| coinflip | 2302 | 49.9 | 50.5 | $-1233.70 | -5.4% | $-233.70 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 1358 | 48.8 | 51.3 | $-1314.04 | -9.7% | $-314.04 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 2302 | 50.2 | 51.9 | $-1620.91 | -7.0% | $-620.91 | -3.5 | done | losing for real |
| always_up | 2302 | 47.0 | 49.9 | $-2294.22 | -10.0% | $-1294.22 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3623 | 47.8 | 49.3 | $-2661.00 |
| ETH | 3989 | 48.0 | 48.6 | $-2733.06 |
| SOL | 4159 | 47.8 | 48.8 | $-3118.45 |
| XRP | 4208 | 48.5 | 48.6 | $-2257.11 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
