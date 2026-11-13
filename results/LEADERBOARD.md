# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 1:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 215 windows, 5619 settled trades, 53 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 555 | 56.2 | 52.7 | $+201.96 | +3.6% | $1201.96 | +0.9 | done | can't tell from luck |
| reversal_60m_0.30pct | 436 | 54.6 | 52.7 | $+28.54 | +0.7% | $1028.54 | +0.1 | done | can't tell from luck |
| value_ev20 | 105 | 34.3 | 37.0 | $-126.06 | -12.0% | $873.94 | -1.0 | Sun 6:15 AM | too few trades (105/200) |
| value_ev10 | 279 | 37.3 | 40.9 | $-358.28 | -12.8% | $641.72 | -1.9 | done | can't tell from luck |
| trend_filter | 291 | 45.0 | 50.0 | $-389.07 | -13.4% | $610.93 | -2.3 | done | losing for real |
| value_ev5 | 406 | 39.4 | 42.6 | $-470.08 | -11.6% | $529.92 | -2.1 | done | losing for real |
| momentum_5m_0.00pct | 852 | 50.6 | 51.5 | $-485.79 | -5.7% | $514.21 | -1.7 | done | can't tell from luck |
| coinflip | 852 | 50.1 | 51.0 | $-496.84 | -5.8% | $503.16 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 436 | 45.4 | 49.6 | $-530.73 | -12.2% | $469.27 | -2.6 | done | losing for real |
| momentum_15m_0.10pct | 555 | 43.8 | 49.7 | $-848.26 | -15.3% | $151.74 | -3.7 | done | losing for real |
| always_up | 852 | 46.7 | 50.2 | $-945.23 | -11.1% | $54.77 | -3.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1251 | 46.2 | 49.7 | $-1286.22 |
| ETH | 1401 | 46.5 | 48.9 | $-1321.17 |
| SOL | 1448 | 48.0 | 49.3 | $-1178.93 |
| XRP | 1519 | 49.6 | 49.3 | $-633.54 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
