# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 7:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 238 windows, 6203 settled trades, 43 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 611 | 56.5 | 52.5 | $+260.90 | +4.3% | $1260.90 | +1.1 | done | can't tell from luck |
| reversal_60m_0.30pct | 484 | 54.1 | 52.3 | $-4.50 | -0.1% | $995.50 | -0.0 | done | can't tell from luck |
| value_ev20 | 113 | 34.5 | 36.6 | $-110.27 | -9.8% | $889.73 | -0.8 | Sun 8:45 AM | too few trades (113/200) |
| value_ev10 | 302 | 38.1 | 40.8 | $-313.26 | -10.4% | $686.74 | -1.5 | done | can't tell from luck |
| value_ev5 | 440 | 39.8 | 42.5 | $-450.33 | -10.2% | $549.67 | -1.9 | done | can't tell from luck |
| trend_filter | 326 | 45.1 | 50.2 | $-453.21 | -13.9% | $546.79 | -2.6 | done | losing for real |
| momentum_60m_0.30pct | 484 | 45.9 | 49.9 | $-577.77 | -11.9% | $422.23 | -2.7 | done | losing for real |
| coinflip | 944 | 49.6 | 51.0 | $-636.22 | -6.7% | $363.78 | -2.1 | done | losing for real |
| momentum_5m_0.00pct | 944 | 49.6 | 51.5 | $-712.17 | -7.5% | $287.83 | -2.4 | done | losing for real |
| always_up | 944 | 47.5 | 50.4 | $-946.41 | -10.0% | $53.59 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 611 | 43.5 | 49.8 | $-969.19 | -15.9% | $30.81 | -4.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1386 | 46.3 | 49.7 | $-1436.37 |
| ETH | 1545 | 46.7 | 49.0 | $-1539.39 |
| SOL | 1602 | 48.2 | 49.4 | $-1218.09 |
| XRP | 1670 | 49.1 | 49.2 | $-718.58 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
