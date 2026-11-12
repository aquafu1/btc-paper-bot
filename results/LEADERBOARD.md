# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 12:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 122 windows, 3109 settled trades, 39 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 231 | 61.5 | 53.0 | $+318.69 | +13.8% | $1318.69 | +2.2 | done | real edge? (z>=2) |
| reversal_15m_0.10pct | 294 | 56.5 | 51.8 | $+196.59 | +6.7% | $1196.59 | +1.2 | done | can't tell from luck |
| momentum_5m_0.00pct | 480 | 52.1 | 50.9 | $-84.05 | -1.8% | $915.95 | -0.4 | done | can't tell from luck |
| value_ev10 | 163 | 38.0 | 40.4 | $-168.93 | -10.4% | $831.07 | -1.1 | Thu 7:15 AM | too few trades (163/200) |
| value_ev20 | 61 | 26.2 | 36.4 | $-182.65 | -29.9% | $817.35 | -1.9 | Sun 2:00 AM | too few trades (61/200) |
| coinflip | 480 | 50.4 | 51.1 | $-273.05 | -5.7% | $726.95 | -1.3 | done | can't tell from luck |
| trend_filter | 164 | 40.9 | 49.1 | $-324.23 | -19.8% | $675.77 | -2.5 | Thu 7:00 AM | too few trades (164/200) |
| value_ev5 | 231 | 37.7 | 42.0 | $-328.04 | -14.2% | $671.96 | -1.9 | done | can't tell from luck |
| momentum_15m_0.10pct | 294 | 43.5 | 50.3 | $-472.16 | -16.1% | $527.84 | -2.8 | done | losing for real |
| momentum_60m_0.30pct | 231 | 38.5 | 49.2 | $-547.49 | -23.7% | $452.51 | -3.6 | done | losing for real |
| always_up | 480 | 45.8 | 50.1 | $-611.46 | -12.7% | $388.54 | -2.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 668 | 45.1 | 49.5 | $-744.73 |
| ETH | 762 | 45.1 | 48.8 | $-822.77 |
| SOL | 827 | 48.4 | 48.6 | $-577.27 |
| XRP | 852 | 49.8 | 48.9 | $-332.01 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
