# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 2:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 218 windows, 5699 settled trades, 47 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 564 | 56.2 | 52.7 | $+199.51 | +3.5% | $1199.51 | +0.9 | done | can't tell from luck |
| reversal_60m_0.30pct | 445 | 55.3 | 52.7 | $+90.48 | +2.0% | $1090.48 | +0.5 | done | can't tell from luck |
| value_ev20 | 105 | 34.3 | 37.0 | $-126.06 | -12.0% | $873.94 | -1.0 | Sun 7:45 AM | too few trades (105/200) |
| value_ev10 | 280 | 37.1 | 40.9 | $-368.28 | -13.2% | $631.72 | -1.9 | done | can't tell from luck |
| trend_filter | 296 | 44.3 | 50.0 | $-439.07 | -14.8% | $560.93 | -2.6 | done | losing for real |
| value_ev5 | 408 | 39.2 | 42.7 | $-490.08 | -12.0% | $509.92 | -2.2 | done | losing for real |
| coinflip | 864 | 50.1 | 51.0 | $-510.22 | -5.9% | $489.78 | -1.8 | done | can't tell from luck |
| momentum_5m_0.00pct | 864 | 50.3 | 51.5 | $-526.11 | -6.1% | $473.89 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 445 | 44.7 | 49.6 | $-603.90 | -13.6% | $396.10 | -2.9 | done | losing for real |
| momentum_15m_0.10pct | 564 | 43.8 | 49.7 | $-862.03 | -15.3% | $137.97 | -3.7 | done | losing for real |
| always_up | 864 | 46.6 | 50.3 | $-982.22 | -11.4% | $17.78 | -3.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1272 | 46.1 | 49.7 | $-1350.64 |
| ETH | 1418 | 46.4 | 48.9 | $-1386.26 |
| SOL | 1470 | 48.0 | 49.4 | $-1200.62 |
| XRP | 1539 | 49.4 | 49.4 | $-680.47 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
