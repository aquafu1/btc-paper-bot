# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 8:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 578 windows, 16016 settled trades, 34 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1360 | 51.1 | 49.6 | $-268.07 | -2.0% | $731.93 | -0.7 | done | can't tell from luck |
| value_ev20 | 313 | 33.2 | 35.2 | $-344.56 | -11.0% | $655.44 | -1.5 | done | can't tell from luck |
| trend_filter | 928 | 50.4 | 51.0 | $-514.64 | -5.5% | $485.36 | -1.7 | done | can't tell from luck |
| value_ev10 | 752 | 37.5 | 39.4 | $-707.94 | -9.4% | $292.06 | -2.1 | done | losing for real |
| reversal_15m_0.10pct | 1629 | 51.0 | 51.0 | $-763.41 | -4.7% | $236.59 | -1.9 | done | can't tell from luck |
| value_ev5 | 1124 | 39.9 | 41.3 | $-853.91 | -7.6% | $146.09 | -2.2 | done | losing for real |
| momentum_15m_0.10pct | 1629 | 49.0 | 49.9 | $-993.04 | -6.1% | $6.96 | -2.5 | done | losing for real |
| coinflip | 2307 | 49.8 | 50.5 | $-1251.50 | -5.4% | $-251.50 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 1360 | 48.9 | 51.3 | $-1299.88 | -9.6% | $-299.88 | -3.6 | done | losing for real |
| momentum_5m_0.00pct | 2307 | 50.3 | 51.9 | $-1609.03 | -7.0% | $-609.03 | -3.5 | done | losing for real |
| always_up | 2307 | 46.9 | 49.8 | $-2344.22 | -10.2% | $-1344.22 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3631 | 47.8 | 49.2 | $-2713.03 |
| ETH | 3997 | 47.9 | 48.6 | $-2783.04 |
| SOL | 4164 | 47.8 | 48.8 | $-3133.61 |
| XRP | 4224 | 48.5 | 48.6 | $-2320.52 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
