# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 8:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 336 windows, 8971 settled trades, 63 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 180 | 37.8 | 36.7 | $-22.79 | -1.3% | $977.21 | -0.1 | Sat 5:45 PM | too few trades (180/200) |
| reversal_60m_0.30pct | 717 | 53.1 | 51.8 | $-113.06 | -1.6% | $886.94 | -0.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 887 | 52.8 | 52.0 | $-246.72 | -2.8% | $753.28 | -0.9 | done | can't tell from luck |
| value_ev10 | 437 | 39.1 | 40.3 | $-283.09 | -6.5% | $716.91 | -1.1 | done | can't tell from luck |
| value_ev5 | 651 | 40.7 | 42.0 | $-447.54 | -6.9% | $552.46 | -1.5 | done | can't tell from luck |
| trend_filter | 487 | 45.4 | 50.3 | $-683.95 | -14.0% | $316.05 | -3.2 | done | losing for real |
| coinflip | 1336 | 50.1 | 50.9 | $-735.77 | -5.5% | $264.23 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 717 | 46.9 | 49.8 | $-742.69 | -10.4% | $257.31 | -2.8 | done | losing for real |
| momentum_15m_0.10pct | 887 | 47.2 | 49.7 | $-805.56 | -9.1% | $194.44 | -2.7 | done | losing for real |
| momentum_5m_0.00pct | 1336 | 48.6 | 51.3 | $-1207.89 | -9.0% | $-207.89 | -3.4 | done | losing for real |
| always_up | 1336 | 47.5 | 50.4 | $-1296.95 | -9.7% | $-296.95 | -3.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2004 | 46.8 | 49.3 | $-1752.11 |
| ETH | 2252 | 47.3 | 48.7 | $-1755.07 |
| SOL | 2338 | 47.9 | 49.3 | $-1819.70 |
| XRP | 2377 | 48.7 | 49.0 | $-1259.13 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
