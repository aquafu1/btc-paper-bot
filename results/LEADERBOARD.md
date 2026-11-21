# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 2:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 985 windows, 27393 settled trades, 35 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 503 | 34.4 | 34.9 | $-265.26 | -5.3% | $734.74 | -0.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 2796 | 51.1 | 50.4 | $-834.44 | -3.0% | $165.56 | -1.6 | done | can't tell from luck |
| value_ev10 | 1253 | 37.6 | 39.1 | $-867.53 | -6.9% | $132.47 | -2.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 2351 | 49.9 | 49.7 | $-1039.15 | -4.4% | $-39.15 | -2.1 | done | losing for real |
| trend_filter | 1643 | 49.7 | 50.9 | $-1162.65 | -7.1% | $-162.65 | -2.9 | done | losing for real |
| value_ev5 | 1895 | 39.6 | 41.0 | $-1234.87 | -6.5% | $-234.87 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 2351 | 50.1 | 50.9 | $-1568.78 | -6.7% | $-568.78 | -3.3 | done | losing for real |
| coinflip | 3935 | 50.3 | 50.3 | $-1701.19 | -4.3% | $-701.19 | -2.7 | done | losing for real |
| momentum_15m_0.10pct | 2796 | 48.9 | 50.3 | $-1923.70 | -6.9% | $-923.70 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 3935 | 50.9 | 51.5 | $-1993.20 | -5.1% | $-993.20 | -3.3 | done | losing for real |
| always_up | 3935 | 46.7 | 49.6 | $-4001.91 | -10.2% | $-3001.91 | -6.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6241 | 48.2 | 49.1 | $-3491.11 |
| ETH | 6810 | 48.0 | 48.5 | $-4437.19 |
| SOL | 7155 | 48.1 | 48.6 | $-4215.17 |
| XRP | 7187 | 48.1 | 48.5 | $-4449.20 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
