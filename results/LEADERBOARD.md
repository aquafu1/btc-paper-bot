# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 3:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 223 windows, 5823 settled trades, 57 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 576 | 56.2 | 52.7 | $+215.26 | +3.7% | $1215.26 | +1.0 | done | can't tell from luck |
| reversal_60m_0.30pct | 453 | 55.2 | 52.6 | $+86.78 | +1.9% | $1086.78 | +0.4 | done | can't tell from luck |
| value_ev20 | 107 | 34.6 | 37.0 | $-115.89 | -10.8% | $884.11 | -0.9 | Sun 8:00 AM | too few trades (107/200) |
| value_ev10 | 288 | 38.2 | 40.9 | $-301.85 | -10.5% | $698.15 | -1.5 | done | can't tell from luck |
| value_ev5 | 417 | 40.0 | 42.7 | $-412.74 | -9.9% | $587.26 | -1.8 | done | can't tell from luck |
| trend_filter | 301 | 44.5 | 50.1 | $-435.99 | -14.5% | $564.01 | -2.5 | done | losing for real |
| momentum_5m_0.00pct | 884 | 50.3 | 51.4 | $-521.10 | -5.9% | $478.90 | -1.8 | done | can't tell from luck |
| coinflip | 884 | 49.8 | 51.0 | $-562.51 | -6.4% | $437.49 | -2.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 453 | 44.8 | 49.7 | $-613.21 | -13.5% | $386.79 | -2.9 | done | losing for real |
| momentum_15m_0.10pct | 576 | 43.8 | 49.6 | $-869.51 | -15.1% | $130.49 | -3.7 | done | losing for real |
| always_up | 884 | 46.7 | 50.2 | $-970.41 | -11.0% | $29.59 | -3.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1301 | 46.4 | 49.7 | $-1273.36 |
| ETH | 1447 | 46.6 | 49.0 | $-1378.79 |
| SOL | 1505 | 48.0 | 49.4 | $-1200.76 |
| XRP | 1570 | 49.4 | 49.3 | $-648.27 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
