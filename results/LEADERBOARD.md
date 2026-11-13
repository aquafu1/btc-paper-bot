# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 2:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 216 windows, 5644 settled trades, 55 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 557 | 56.2 | 52.7 | $+203.32 | +3.7% | $1203.32 | +0.9 | done | can't tell from luck |
| reversal_60m_0.30pct | 440 | 54.8 | 52.6 | $+50.20 | +1.1% | $1050.20 | +0.3 | done | can't tell from luck |
| value_ev20 | 105 | 34.3 | 37.0 | $-126.06 | -12.0% | $873.94 | -1.0 | Sun 6:45 AM | too few trades (105/200) |
| value_ev10 | 279 | 37.3 | 40.9 | $-358.28 | -12.8% | $641.72 | -1.9 | done | can't tell from luck |
| trend_filter | 292 | 44.9 | 50.0 | $-399.07 | -13.7% | $600.93 | -2.4 | done | losing for real |
| value_ev5 | 406 | 39.4 | 42.6 | $-470.08 | -11.6% | $529.92 | -2.1 | done | losing for real |
| coinflip | 856 | 50.2 | 51.0 | $-479.72 | -5.6% | $520.28 | -1.7 | done | can't tell from luck |
| momentum_5m_0.00pct | 856 | 50.6 | 51.5 | $-485.49 | -5.7% | $514.51 | -1.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 440 | 45.2 | 49.6 | $-553.90 | -12.6% | $446.10 | -2.7 | done | losing for real |
| momentum_15m_0.10pct | 557 | 43.8 | 49.7 | $-849.33 | -15.2% | $150.67 | -3.7 | done | losing for real |
| always_up | 856 | 46.6 | 50.3 | $-968.41 | -11.3% | $31.59 | -3.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1258 | 46.3 | 49.7 | $-1280.48 |
| ETH | 1406 | 46.6 | 48.9 | $-1320.69 |
| SOL | 1453 | 48.0 | 49.3 | $-1164.83 |
| XRP | 1527 | 49.4 | 49.3 | $-670.81 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
