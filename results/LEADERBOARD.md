# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 9:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 628 windows, 17370 settled trades, 32 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1466 | 51.2 | 49.5 | $-177.87 | -1.2% | $822.13 | -0.5 | done | can't tell from luck |
| value_ev20 | 330 | 33.9 | 35.3 | $-274.70 | -8.3% | $725.30 | -1.2 | done | can't tell from luck |
| trend_filter | 1006 | 50.1 | 50.8 | $-573.57 | -5.7% | $426.43 | -1.8 | done | can't tell from luck |
| value_ev10 | 803 | 38.2 | 39.5 | $-590.20 | -7.3% | $409.80 | -1.7 | done | can't tell from luck |
| value_ev5 | 1216 | 40.5 | 41.4 | $-740.48 | -6.1% | $259.52 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 1781 | 50.9 | 51.0 | $-821.94 | -4.6% | $178.06 | -2.0 | done | can't tell from luck |
| momentum_15m_0.10pct | 1781 | 49.1 | 49.9 | $-997.72 | -5.6% | $2.28 | -2.4 | done | losing for real |
| coinflip | 2507 | 50.1 | 50.5 | $-1184.67 | -4.7% | $-184.67 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 1466 | 48.8 | 51.4 | $-1399.32 | -9.5% | $-399.32 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 2507 | 50.3 | 51.7 | $-1570.19 | -6.3% | $-570.19 | -3.2 | done | losing for real |
| always_up | 2507 | 47.4 | 49.6 | $-2164.60 | -8.6% | $-1164.60 | -4.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3939 | 48.2 | 49.2 | $-2458.96 |
| ETH | 4345 | 48.1 | 48.6 | $-2669.45 |
| SOL | 4514 | 47.9 | 48.8 | $-3031.97 |
| XRP | 4572 | 48.4 | 48.5 | $-2334.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
