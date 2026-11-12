# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 6:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 149 windows, 3766 settled trades, 56 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 264 | 59.5 | 52.9 | $+256.73 | +9.7% | $1256.73 | +1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 362 | 56.4 | 52.3 | $+188.73 | +5.2% | $1188.73 | +1.0 | done | can't tell from luck |
| momentum_5m_0.00pct | 588 | 52.7 | 51.3 | $-95.44 | -1.6% | $904.56 | -0.4 | done | can't tell from luck |
| value_ev20 | 74 | 32.4 | 37.2 | $-143.54 | -19.4% | $856.46 | -1.4 | Sun 1:30 AM | too few trades (74/200) |
| coinflip | 588 | 51.2 | 50.9 | $-248.14 | -4.2% | $751.86 | -1.1 | done | can't tell from luck |
| value_ev10 | 198 | 36.9 | 40.7 | $-282.43 | -14.3% | $717.57 | -1.8 | Thu 7:00 AM | too few trades (198/200) |
| trend_filter | 189 | 42.3 | 49.3 | $-327.78 | -17.3% | $672.22 | -2.4 | Thu 9:00 AM | too few trades (189/200) |
| value_ev5 | 289 | 38.1 | 42.4 | $-419.73 | -14.5% | $580.27 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 264 | 40.5 | 49.4 | $-542.03 | -20.5% | $457.97 | -3.4 | done | losing for real |
| momentum_15m_0.10pct | 362 | 43.6 | 50.0 | $-570.91 | -15.8% | $429.09 | -3.1 | done | losing for real |
| always_up | 588 | 45.9 | 49.9 | $-737.15 | -12.5% | $262.85 | -3.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 807 | 45.8 | 49.6 | $-831.58 |
| ETH | 932 | 45.4 | 48.8 | $-1042.97 |
| SOL | 991 | 48.3 | 48.8 | $-731.03 |
| XRP | 1036 | 50.4 | 49.1 | $-316.13 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
