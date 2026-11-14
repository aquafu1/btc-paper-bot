# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 2:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 361 windows, 9756 settled trades, 33 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 187 | 37.4 | 36.5 | $-29.59 | -1.6% | $970.41 | -0.2 | Sat 9:00 PM | too few trades (187/200) |
| value_ev10 | 472 | 40.7 | 40.3 | $-119.55 | -2.5% | $880.45 | -0.5 | done | can't tell from luck |
| value_ev5 | 700 | 42.0 | 42.0 | $-261.05 | -3.7% | $738.95 | -0.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 967 | 52.0 | 52.1 | $-407.37 | -4.2% | $592.63 | -1.4 | done | can't tell from luck |
| reversal_60m_0.30pct | 803 | 51.1 | 52.0 | $-457.12 | -5.7% | $542.88 | -1.7 | done | can't tell from luck |
| trend_filter | 540 | 48.3 | 50.6 | $-470.88 | -8.7% | $529.12 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 803 | 48.9 | 49.7 | $-483.76 | -6.0% | $516.24 | -1.7 | done | can't tell from luck |
| momentum_15m_0.10pct | 967 | 48.0 | 49.7 | $-688.49 | -7.1% | $311.51 | -2.2 | done | losing for real |
| coinflip | 1439 | 50.2 | 50.7 | $-700.21 | -4.9% | $299.79 | -1.9 | done | can't tell from luck |
| momentum_5m_0.00pct | 1439 | 49.5 | 51.5 | $-1077.06 | -7.5% | $-77.06 | -2.9 | done | losing for real |
| always_up | 1439 | 46.1 | 50.7 | $-1822.59 | -12.7% | $-822.59 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2191 | 47.3 | 49.3 | $-1722.71 |
| ETH | 2457 | 47.7 | 48.8 | $-1745.34 |
| SOL | 2523 | 48.1 | 49.4 | $-1858.92 |
| XRP | 2585 | 48.9 | 49.1 | $-1190.71 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
