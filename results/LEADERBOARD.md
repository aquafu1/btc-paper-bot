# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 6:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 186 windows, 4731 settled trades, 46 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 348 | 59.8 | 53.0 | $+341.49 | +9.8% | $1341.49 | +2.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 459 | 57.7 | 52.4 | $+324.69 | +7.1% | $1324.69 | +1.6 | done | can't tell from luck |
| value_ev20 | 88 | 34.1 | 36.7 | $-128.58 | -14.6% | $871.42 | -1.1 | Sun 11:15 AM | too few trades (88/200) |
| momentum_5m_0.00pct | 736 | 51.5 | 51.3 | $-274.99 | -3.7% | $725.01 | -1.1 | done | can't tell from luck |
| value_ev10 | 237 | 37.6 | 40.7 | $-305.34 | -12.9% | $694.66 | -1.7 | done | can't tell from luck |
| coinflip | 736 | 50.3 | 50.9 | $-409.33 | -5.6% | $590.67 | -1.6 | done | can't tell from luck |
| value_ev5 | 348 | 39.1 | 42.4 | $-430.83 | -12.4% | $569.17 | -2.1 | done | losing for real |
| trend_filter | 236 | 41.1 | 49.4 | $-462.98 | -19.6% | $537.02 | -3.0 | done | losing for real |
| momentum_60m_0.30pct | 348 | 40.2 | 49.1 | $-746.81 | -21.5% | $253.19 | -4.1 | done | losing for real |
| momentum_15m_0.10pct | 459 | 42.3 | 49.7 | $-832.93 | -18.1% | $167.07 | -4.0 | done | losing for real |
| always_up | 736 | 46.6 | 50.1 | $-845.23 | -11.5% | $154.77 | -3.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1033 | 45.9 | 49.5 | $-1054.44 |
| ETH | 1175 | 46.0 | 48.8 | $-1285.90 |
| SOL | 1230 | 47.9 | 49.0 | $-1017.64 |
| XRP | 1293 | 50.0 | 49.2 | $-412.86 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
