# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 12:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 208 windows, 5406 settled trades, 52 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 531 | 57.3 | 52.8 | $+278.02 | +5.2% | $1278.02 | +1.3 | done | can't tell from luck |
| reversal_60m_0.30pct | 413 | 55.7 | 52.7 | $+107.37 | +2.6% | $1107.37 | +0.6 | done | can't tell from luck |
| value_ev20 | 104 | 33.7 | 36.9 | $-137.53 | -13.2% | $862.47 | -1.1 | Sun 4:00 AM | too few trades (104/200) |
| value_ev10 | 270 | 36.7 | 40.8 | $-377.15 | -14.0% | $622.85 | -2.0 | done | can't tell from luck |
| coinflip | 824 | 50.6 | 51.0 | $-412.69 | -5.0% | $587.31 | -1.5 | done | can't tell from luck |
| trend_filter | 279 | 43.7 | 49.8 | $-434.12 | -15.6% | $565.88 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 824 | 50.6 | 51.4 | $-459.38 | -5.6% | $540.62 | -1.7 | done | can't tell from luck |
| value_ev5 | 393 | 38.7 | 42.5 | $-508.67 | -12.9% | $491.33 | -2.3 | done | losing for real |
| momentum_60m_0.30pct | 413 | 44.3 | 49.5 | $-588.00 | -14.2% | $412.00 | -2.9 | done | losing for real |
| momentum_15m_0.10pct | 531 | 42.7 | 49.5 | $-904.15 | -17.0% | $95.85 | -4.0 | done | losing for real |
| always_up | 824 | 45.6 | 50.2 | $-1090.92 | -13.2% | $-90.92 | -3.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1200 | 46.1 | 49.6 | $-1243.10 |
| ETH | 1349 | 46.3 | 48.8 | $-1325.83 |
| SOL | 1395 | 47.6 | 49.3 | $-1250.47 |
| XRP | 1462 | 49.2 | 49.2 | $-707.83 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
