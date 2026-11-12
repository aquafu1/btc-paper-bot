# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 8:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 155 windows, 3930 settled trades, 51 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 282 | 59.6 | 53.1 | $+267.57 | +9.5% | $1267.57 | +1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 378 | 57.1 | 52.3 | $+239.98 | +6.3% | $1239.98 | +1.3 | done | can't tell from luck |
| momentum_5m_0.00pct | 613 | 52.4 | 51.3 | $-142.48 | -2.3% | $857.52 | -0.6 | done | can't tell from luck |
| value_ev20 | 74 | 32.4 | 37.2 | $-143.54 | -19.4% | $856.46 | -1.4 | Sun 6:15 AM | too few trades (74/200) |
| coinflip | 613 | 50.9 | 50.9 | $-294.03 | -4.8% | $705.97 | -1.2 | done | can't tell from luck |
| value_ev10 | 201 | 36.8 | 40.8 | $-295.12 | -14.7% | $704.88 | -1.8 | done | can't tell from luck |
| trend_filter | 200 | 41.5 | 49.2 | $-381.61 | -19.1% | $618.39 | -2.7 | done | losing for real |
| value_ev5 | 296 | 38.2 | 42.5 | $-430.38 | -14.5% | $569.62 | -2.3 | done | losing for real |
| momentum_60m_0.30pct | 282 | 40.4 | 49.3 | $-588.61 | -20.9% | $411.39 | -3.6 | done | losing for real |
| momentum_15m_0.10pct | 378 | 42.9 | 50.0 | $-658.84 | -17.4% | $341.16 | -3.5 | done | losing for real |
| always_up | 613 | 46.0 | 50.1 | $-779.00 | -12.7% | $221.00 | -3.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 846 | 46.0 | 49.7 | $-887.46 |
| ETH | 978 | 45.5 | 48.9 | $-1107.47 |
| SOL | 1033 | 48.1 | 48.9 | $-812.83 |
| XRP | 1073 | 50.1 | 49.1 | $-398.31 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
