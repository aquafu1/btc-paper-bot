# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 3:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 270 windows, 7058 settled trades, 67 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 693 | 55.0 | 52.3 | $+81.64 | +1.2% | $1081.64 | +0.3 | done | can't tell from luck |
| value_ev20 | 127 | 35.4 | 37.0 | $-111.59 | -8.8% | $888.41 | -0.8 | Sun 8:45 AM | too few trades (127/200) |
| reversal_60m_0.30pct | 561 | 52.9 | 52.3 | $-156.75 | -2.8% | $843.25 | -0.7 | done | can't tell from luck |
| value_ev10 | 339 | 37.8 | 40.8 | $-372.60 | -11.0% | $627.40 | -1.7 | done | can't tell from luck |
| trend_filter | 368 | 46.5 | 50.2 | $-430.18 | -11.7% | $569.82 | -2.3 | done | losing for real |
| value_ev5 | 500 | 40.0 | 42.4 | $-486.63 | -9.7% | $513.37 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 561 | 47.1 | 49.6 | $-561.95 | -10.0% | $438.05 | -2.4 | done | losing for real |
| momentum_5m_0.00pct | 1072 | 50.0 | 51.4 | $-733.08 | -6.8% | $266.92 | -2.3 | done | losing for real |
| coinflip | 1072 | 49.3 | 50.9 | $-774.65 | -7.2% | $225.35 | -2.4 | done | losing for real |
| momentum_15m_0.10pct | 693 | 45.0 | 49.7 | $-913.02 | -13.2% | $86.98 | -3.5 | done | losing for real |
| always_up | 1072 | 47.4 | 50.2 | $-1052.65 | -9.8% | $-52.65 | -3.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1571 | 46.6 | 49.6 | $-1598.03 |
| ETH | 1761 | 46.9 | 49.0 | $-1706.21 |
| SOL | 1829 | 48.3 | 49.3 | $-1372.25 |
| XRP | 1897 | 49.0 | 49.1 | $-834.97 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
